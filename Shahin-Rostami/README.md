# NYC Subway Ridership Prediction

This project uses a Random Forest regression model to predict daily
subway ridership in New York City based on features like day of the
week, temperature, and rainfall. The code is implemented in Python and
includes data preprocessing, model training, evaluation, and
visualization.

## Project Overview

The goal of this project is to predict subway passenger counts using
historical data or synthetic data if the real dataset is unavailable.
The model leverages features such as: - **Day of the week**: Captures
weekly patterns (e.g., lower ridership on weekends). - **Temperature**:
Influences passenger behavior (e.g., higher temperatures may increase
ridership). - **Rainfall**: Affects ridership negatively (e.g., heavy
rain reduces passengers).

The model is trained on a dataset, evaluated using metrics like R²,
RMSE, and MAE, and used to predict ridership for the next three days.
Results are visualized in a time series plot comparing actual
vs. predicted passenger counts.

## Features

-   **Data Source**: Attempts to download a real NYC subway ridership
    dataset from a public URL. If unavailable, generates synthetic data.
-   **Data Preprocessing**: Handles missing columns, converts dates, and
    creates features like day of the week.
-   **Model**: Random Forest Regressor with 300 estimators for robust
    predictions.
-   **Evaluation**: Calculates R² score, RMSE, and MAE to assess model
    performance.
-   **Prediction**: Forecasts subway ridership for the next three days.
-   **Visualization**: Plots actual vs. predicted passenger counts over
    time.

## Requirements

To run this project, ensure you have the following Python libraries
installed:

``` bash
pip install pandas numpy matplotlib scikit-learn
```

## File Structure

-   `task_1.py`: Main Python script containing the data processing,
    model training, evaluation, prediction, and visualization code.
-   `README.md`: This file, providing an overview of the project.

## Dataset

The script attempts to use a real NYC subway ridership dataset from:

    https://raw.githubusercontent.com/datablist/sample-csv-files/main/files/people/nyc-subway-ridership.csv

If the dataset is unavailable, it generates synthetic data with the
following features: - **Date**: Daily dates for 2024. - **Day of Week**:
Derived from the date (0 = Monday, 6 = Sunday). - **Temperature**:
Random normal distribution (mean = 20°C, std = 8). - **Rainfall**:
Random normal distribution (mean = 2mm, std = 1, absolute values). -
**Passengers**: Calculated based on temperature, rainfall, and day of
the week, with added noise.

## Model Details

-   **Algorithm**: Random Forest Regressor (`n_estimators=300`,
    `random_state=42`).
-   **Features**: `day_of_week`, `temperature`, `rainfall`.
-   **Target**: `passengers` (daily subway ridership).
-   **Train-Test Split**: 80% training, 20% testing (no shuffling to
    preserve time series order).

## Outputs

-   **Model Performance Metrics**:

    -   R² Score: Measures the proportion of variance explained by the
        model.
    -   RMSE: Root Mean Squared Error, indicating prediction error
        magnitude.
    -   MAE: Mean Absolute Error, showing average prediction error.

-   **Future Predictions**: Passenger counts for the next three days,
    based on randomly generated temperature and rainfall.

-   **Visualization**: A time series plot showing actual vs. predicted
    passenger counts for the test set.

## Example Output

    Model Performance:
    R² Score: 0.XXXX
    RMSE: XXX,XXX
    MAE: XX,XXX

    Prediction for next 3 days:
             date  predicted_passengers
    0  2025-01-01           XXX,XXX
    1  2025-01-02           XXX,XXX
    2  2025-01-03           XXX,XXX

## Future Improvements

-   Incorporate additional features (e.g., holidays, events, or
    station-specific data).
-   Experiment with other models (e.g., XGBoost, LSTM for time series).
-   Enhance visualization with interactive plots (e.g., using Plotly).
-   Add cross-validation for more robust model evaluation.
