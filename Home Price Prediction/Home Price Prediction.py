import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt


file_path = "C:/Users/Asus/Desktop/home price.csv"
df = pd.read_csv(file_path)
print("Data successfully loaded.")

#feature engi
NUMERIC_FEATURES = [
    'Gr Liv Area', 'Overall Qual', 'Year Built', 'Total Bsmt SF',
    'Full Bath', 'Garage Cars', 'TotRms AbvGrd'
]
TARGET_COLUMN = 'SalePrice'
CATEGORICAL_FEATURES = ['Neighborhood']


current_year = 2010
df['HouseAge'] = current_year - df['Year Built']
NUMERIC_FEATURES.remove('Year Built')
NUMERIC_FEATURES.append('HouseAge')

#
ALL_FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
data_combined = pd.concat([df[ALL_FEATURES], df[TARGET_COLUMN]], axis=1).dropna()
X = data_combined[ALL_FEATURES]
Y = data_combined[TARGET_COLUMN]

#One-Hot Encoding
X_encoded = pd.get_dummies(X, columns=CATEGORICAL_FEATURES, drop_first=True)
print(f"Total features after One-Hot Encoding: {X_encoded.shape[1]}")

#spiliting
X_train, X_test, Y_train, Y_test = train_test_split(
    X_encoded,
    Y,
    test_size=0.2,
    random_state=42
)

print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

#Random Forest Regressor


model = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train, Y_train)


Y_pred = model.predict(X_test)

print("\nModel successfully trained using Random Forest Regressor.")

#metrics
rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))
mae = mean_absolute_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("\n--- Model Performance Metrics (Random Forest) ---")
print(f"RMSE (Root Mean Squared Error): ${rmse:,.2f}")
print(f"MAE (Mean Absolute Error): ${mae:,.2f}")
print(f"R-squared (Coefficient of Determination): {r2:.4f}")
print(f"\nInterpretation: The Random Forest model explains {r2*100:.2f}% of price variation.")

#plot
plt.figure(figsize=(10, 6))

plt.scatter(Y_test, Y_pred, color='blue', alpha=0.5, label='Actual vs. Predicted Price')


max_val = max(Y_test.max(), Y_pred.max())
min_val = min(Y_test.min(), Y_pred.min())
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', linewidth=2, label='Perfect Prediction Line (Y=X)')


plt.title('Actual vs. Predicted House Prices (Random Forest)')
plt.xlabel('Actual Price ($)', fontsize=12)
plt.ylabel('Predicted Price ($)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("\nFull project execution completed.")