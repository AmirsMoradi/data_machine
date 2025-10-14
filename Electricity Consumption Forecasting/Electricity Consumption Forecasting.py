import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import holidays



POWER_FILE_PATH = r"C:\Users\Asus\Desktop\household_power_consumption.txt"
WEATHER_FILE_PATH = 'sceaux_historical_weather_2006_2010.csv'


plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 6)
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

#loading and cleaning data
def load_and_clean_power_data(file_path):
    power_df = pd.read_csv(
        file_path, sep=';', low_memory=False, parse_dates={'Datetime': ['Date', 'Time']}, index_col=['Datetime']
    )
    power_df.replace('?', np.nan, inplace=True)
    for col in power_df.columns:
        power_df[col] = pd.to_numeric(power_df[col], errors='coerce')
    power_df.dropna(inplace=True)
    daily_power = power_df['Global_active_power'].resample('D').sum().to_frame('Daily_Consumption_kWh')
    return daily_power[daily_power['Daily_Consumption_kWh'] > 0].copy()

def load_and_clean_weather_data(file_path):
    weather_df = pd.read_csv(file_path)
    TIME_COL = 'time'
    TEMP_COL = 'temperature_2m'
    HUMIDITY_COL = 'relative_humidity_2m'
    weather_df[TIME_COL] = pd.to_datetime(weather_df[TIME_COL])
    weather_df.set_index(TIME_COL, inplace=True)
    daily_weather = weather_df[[TEMP_COL, HUMIDITY_COL]].resample('D').mean()
    daily_weather.rename(columns={TEMP_COL: 'Avg_Temp', HUMIDITY_COL: 'Avg_Humidity'}, inplace=True)
    return daily_weather.dropna().copy()

#data merged
#feature engi
daily_power_df = load_and_clean_power_data(POWER_FILE_PATH)
daily_weather_df = load_and_clean_weather_data(WEATHER_FILE_PATH)

df = pd.merge(daily_power_df, daily_weather_df, left_index=True, right_index=True, how='inner')


df['dayofweek'] = df.index.dayofweek
df['dayofyear'] = df.index.dayofyear
df['month'] = df.index.month
df['year'] = df.index.year
df['is_weekend'] = (df.index.dayofweek >= 5).astype(int)

fr_holidays = holidays.country_holidays('FR', years=df.index.year.unique())
df['is_holiday'] = df.index.map(lambda date: date.date() in fr_holidays).astype(int)

df['Consumption_Lag_1'] = df['Daily_Consumption_kWh'].shift(1)
df['Consumption_Lag_7'] = df['Daily_Consumption_kWh'].shift(7)

df['Avg_Temp_Lag_7'] = df['Avg_Temp'].shift(7)
df['Avg_Humidity_Lag_7'] = df['Avg_Humidity'].shift(7)

df.drop(columns=['Avg_Temp', 'Avg_Humidity'], inplace=True)
df.dropna(inplace=True)

#spliting
FORECAST_HORIZON = 1
TARGET = 'Daily_Consumption_kWh'
FEATURES = [
    'dayofweek', 'dayofyear', 'month', 'year', 'is_weekend', 'is_holiday',
    'Consumption_Lag_1', 'Consumption_Lag_7',
    'Avg_Temp_Lag_7', 'Avg_Humidity_Lag_7'
]

train_data = df.iloc[:-FORECAST_HORIZON].copy()
test_data = df.iloc[-FORECAST_HORIZON:].copy()

X_train = train_data[FEATURES]
y_train = train_data[TARGET]
X_test = test_data[FEATURES]
y_test = test_data[TARGET]

#XGBOOST
model = XGBRegressor(
    n_estimators=1000,
    learning_rate=0.02,
    max_depth=8,
    subsample=0.7,
    colsample_bytree=0.7,
    random_state=42
)
model.fit(X_train, y_train)

#predicting last 30 days
y_pred_1day = model.predict(X_test)

test_window = min(30, len(df) // 5)
df_window = df.iloc[-test_window:].copy()
X_test_full = df_window[FEATURES]
y_test_full = df_window[TARGET]
y_pred_full = model.predict(X_test_full)

df_window['Prediction'] = y_pred_full
rmse_full = np.sqrt(mean_squared_error(y_test_full, y_pred_full))
mae_full = mean_absolute_error(y_test_full, y_pred_full)
r2_full = r2_score(y_test_full, y_pred_full)

rmse_1day = np.sqrt(mean_squared_error(y_test, y_pred_1day))
mae_1day = mean_absolute_error(y_test, y_pred_1day)
r2_1day = r2_score(y_test, y_pred_1day)

#printing results

print(f" نتایج پیش‌بینی ۱ روز آینده:")
print(f"   - مصرف واقعی روز آینده: {y_test.values[0]:.2f} kWh")
print(f"   - مصرف پیش‌بینی شده: {y_pred_1day[0]:.2f} kWh")

print(f"\n   --- معیارهای ارزیابی (تست ۱ روزه) ---")
print(f"   - RMSE: {rmse_1day:.4f}")
print(f"   - MAE: {mae_1day:.4f}")
print(f"   - R-Squared (R²): nan")

print(f"\n   --- معیارهای ارزیابی روی {test_window} روز آخر (تنظیم‌شده) ---")
print(f"   - RMSE: {rmse_full:.4f}")
print(f"   - MAE: {mae_full:.4f}")
print(f"   - R-Squared (R²): {r2_full:.4f}")

#visualization

#Actual vs. Predicted Consumption
plt.figure(figsize=(15, 6))
plt.plot(df_window.index, df_window['Daily_Consumption_kWh'], label='Actual Consumption', color='blue', linewidth=2)
plt.plot(df_window.index, df_window['Prediction'], label='Model Prediction', color='red', linestyle='--', linewidth=2)

#highlighting the last day
plt.scatter(df_window.index[-1], df_window['Daily_Consumption_kWh'].iloc[-1], color='black', s=100, zorder=5, label='Actual Last Day')
plt.scatter(df_window.index[-1], df_window['Prediction'].iloc[-1], color='red', s=100, zorder=5, marker='x')


plt.title(f'Daily Consumption Forecasting (Actual vs. Predicted) - Last {test_window} Days', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Daily Consumption (kWh)')
plt.legend(loc='upper right')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Error Plot
errors_full = df_window['Prediction'] - df_window['Daily_Consumption_kWh']
plt.figure(figsize=(15, 4))
plt.plot(df_window.index, errors_full, label='Forecast Error', color='purple')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title(f'Forecast Error Plot (Predicted - Actual) - Last {test_window} Days')
plt.xlabel('Date')
plt.ylabel('Error Value (kWh)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()