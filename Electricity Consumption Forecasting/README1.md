# ⚡ Daily Residential Electricity Consumption Forecasting (XGBoost Time Series Model)
This repository contains the complete solution for a high-accuracy, daily electricity consumption forecasting project using Extreme Gradient Boosting (XGBoost), focused on robust feature engineering and hyperparameter tuning to achieve superior predictive performance.

The final model achieves near-perfect accuracy with an R 
2
  score of 0.9956 on the test set and successfully resolves a major challenge of predicting anomalous low-consumption days (e.g., holidays) by reducing the error on these outliers from ≈250 kWh to just 18.75 kWh.

## 🎯 Project Goal
To build a highly reliable 1-day-ahead forecasting model for residential electricity consumption (kWh) by integrating time-series data with external weather features and specialized lagged variables.

## 🛠️ Methodology and Advanced Features
The project was executed using a rigorous time-series approach to prevent data leakage and ensure model generalizability.

1. Data Processing and Integration
Power Data: Minute-by-minute household power data was loaded, cleaned, and aggregated into Daily Total Consumption (kWh).

Weather Data: Hourly temperature and humidity data were loaded and aggregated into Daily Averages.

Synchronization: Power and Weather data were merged based on shared daily timestamps.

2. Feature Engineering & Leakage Prevention (Crucial Step)
The model's high accuracy stems from advanced feature engineering focused on capturing seasonality and autocorrelation while adhering to real-world forecasting constraints.

Key Features Used:

Temporal Features: dayofweek, month, is_weekend (Captures standard annual and weekly cycles).

Consumption Lag Features: Consumption_Lag_1, Consumption_Lag_7 (Captures the strong 24-hour and 7-day autocorrelations).

Behavioral Feature: is_holiday (Flags non-working days, crucial for consumption dips).

Fixed Weather Lag (Crucial Fix): Avg_Temp_Lag_7, Avg_Humidity_Lag_7 (Uses weather data from the same day last week (Lag_7) to prevent data leakage and leverage the weekly pattern for weather impact).

3. Model & Hyperparameter Tuning
The XGBoostRegressor was selected for its performance on structured data. Optimal parameters were found through iterative tuning:

Final XGBoost Parameters:

n_estimators: 1000

learning_rate: 0.02 (Ensures cautious and precise learning)

max_depth: 8 (Optimal complexity control to prevent overfitting)

subsample: 0.7

colsample_bytree: 0.7

## 📊 Final Results and Performance
The final model was rigorously evaluated on the last 30 days of the dataset, which it had never seen during training, confirming excellent generalization and zero overfitting.

1. General Evaluation (Last 30 Days)
The overall performance demonstrates excellent model generalization and stability:

R-Squared (R 
2
 ): 0.9956 (The model explains 99.56% of the consumption variance - Near-Perfect Fit).

MAE (Mean Absolute Error): 14.6532 kWh (The average daily prediction error is only 14.65 kWh - Extremely High Accuracy).

RMSE: 22.6668

2. Critical 1-Day-Ahead Prediction (Outlier Day)
The key success was resolving the error on a historically anomalous low-consumption day:

Actual Consumption: 1488.10 kWh

Predicted Consumption: 1469.35 kWh

Absolute Error: 18.75 kWh

Conclusion: The final model successfully reduced the initial outlier error (which was ≈250 kWh) to 18.75 kWh, confirming the efficacy of the advanced Lag_7 features combined with optimal hyperparameters.

## 📈 Visual Performance
The plot above visually confirms the exceptional accuracy, showing a near-perfect overlap between the Actual Consumption and the Model Prediction.

<img width="1500" height="400" alt="Figure_2" src="https://github.com/user-attachments/assets/34a6af3d-c557-4734-8f0d-35aaadcd16f3" />
<img width="1500" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/0bed1622-3b15-4629-b842-ab4186a4d1c8" />
