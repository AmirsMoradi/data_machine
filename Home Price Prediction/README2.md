# 🏡 Residential Property Price Prediction using Random Forest
Project Summary
This project documents the development of a highly accurate machine learning model to forecast residential sale prices in Ames, Iowa, using the comprehensive Ames Housing Dataset. Our final solution utilizes a Random Forest Regressor combined with meticulous feature engineering to capture the complex, non-linear dynamics of the real estate market.

The project successfully elevated the predictive accuracy from a basic Linear Regression R 
2
  of 0.75 to an outstanding final score, confirming the model's robustness and reliability for valuation tasks.

## 🎯 Model Performance: Final Results
The final Random Forest model achieved the following performance metrics on the test set:

Key Metrics Summary
R 
2
  (Coefficient of Determination): 0.9146

Interpretation: The model explains 91.46% of the variability in house sale prices. This performance is an increase of +9.18% over the best linear model.

MAE (Mean Absolute Error): \$17,474.95

Interpretation: On average, the model's predictions are off by just $17,475.

RMSE (Root Mean Squared Error): \$26,502.70

Interpretation: This low value confirms the model effectively minimizes the impact of large prediction errors (outliers).

## ⚙️ Methodology and Feature Engineering Pipeline
The significant jump in accuracy was driven by moving from a simple linear model to a sophisticated, non-linear ensemble method, supported by strategic data preparation.

1. Model Implementation Details
Algorithm Used: RandomForestRegressor

Rationale: Selected for its superior ability to model complex, non-linear relationships and its robustness against data noise and outliers compared to linear methods.

Split Strategy: train_test_split (80% Train, 20% Test)

Target Variable (Y): SalePrice

2. Strategic Features Driving Accuracy
The following features were critical in achieving the high R 
2
 :

Quality & Size Factors:

Gr Liv Area, Overall Qual, Total Bsmt SF, Full Bath, Garage Cars.

Locational Premium:

Neighborhood (Crucial for modeling location-based price premiums).

Temporal Feature:

HouseAge (Engineered by calculating 2010−YearBuilt for better capture of depreciation than the raw year).

3. Data Processing Techniques
Categorical Encoding: The Neighborhood feature was processed using One-Hot Encoding (pd.get_dummies) to convert categorical names into a format usable by the model.

Data Integrity: Rows with missing values in the selected critical features were removed.

## 📈 Visualization: Actual vs. Predicted Prices
The final model's performance is visually represented by the scatter plot below. A high-performing model is characterized by data points clustering tightly around the diagonal red line.

The narrow spread of the blue dots around the red line confirms the Random Forest model's low residual error and high confidence across the price spectrum.

<img width="1000" height="600" alt="Figure_3" src="https://github.com/user-attachments/assets/d73bdfda-c41e-4596-8edd-8e82ac14ac7f" />

