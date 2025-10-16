# Air Quality Prediction

This project implements a Random Forest classifier to predict air
quality levels (Good, Moderate, Bad) based on synthetic air quality
data, including pollutants like PM2.5, PM10, NO2, CO, and O3. The code
includes data generation, model training, evaluation, and visualization
of predictions.

## Project Overview

The goal is to create a synthetic dataset for the past 100 days and use
it to train a model that forecasts air quality for the next seven days.
Air quality labels are assigned based on pollutant thresholds, and the
model's performance is evaluated using accuracy, F1 score, and a
confusion matrix. The 7-day forecast is visualized with PM2.5 levels and
predicted air quality labels.

## Features

-   **Data Generation**: Creates synthetic air quality data for 100 days
    with random pollutant levels.
-   **Labeling**: Classifies air quality into 'Good', 'Moderate', or
    'Bad' based on pollutant thresholds.
-   **Model**: Random Forest Classifier with 200 estimators for air
    quality prediction.
-   **Evaluation**: Measures accuracy and F1 score, with a confusion
    matrix for detailed analysis.
-   **Prediction**: Forecasts air quality for the next seven days.
-   **Visualization**: Plots a confusion matrix and a 7-day forecast
    with PM2.5 levels and quality labels.

## Requirements

To run this project, ensure you have the following Python libraries
installed:

``` bash
pip install numpy pandas matplotlib scikit-learn
```

## File Structure

-   `task_2.py`: Main Python script containing data generation, model
    training, evaluation, prediction, and visualization code.
-   `README.md`: This file, providing an overview of the project.

## Dataset

The script generates a synthetic dataset with the following features: -
**Date**: Daily dates for the past 100 days. - **PM2.5**: Particulate
matter (10-200 µg/m³). - **PM10**: Particulate matter (20-300 µg/m³). -
**NO2**: Nitrogen dioxide (5-150 µg/m³). - **CO**: Carbon monoxide
(0.2-2.0 mg/m³). - **O3**: Ozone (10-120 µg/m³). - **AirQuality**:
Classified as 'Good', 'Moderate', or 'Bad' based on pollutant levels.

## Model Details

-   **Algorithm**: Random Forest Classifier (`n_estimators=200`,
    `random_state=42`).
-   **Features**: `PM2.5`, `PM10`, `NO2`, `CO`, `O3`.
-   **Target**: `AirQuality` (categorical: Good, Moderate, Bad).
-   **Train-Test Split**: 80% training, 20% testing.

## Outputs

-   **Model Performance Metrics**:
    -   Accuracy: Proportion of correct predictions.
    -   F1 Score: Weighted average of precision and recall.
-   **Confusion Matrix**: Visual representation of true vs. predicted
    labels.
-   **7-Day Forecast**: Table and plot showing predicted air quality and
    PM2.5 levels for the next seven days.

## Example Output

    Model Performance:
    Accuracy: 0.XXX
    F1 Score: 0.XXX

-   **7-Day Forecast Plot**: Scatter plot with PM2.5 levels colored by
    predicted air quality (Green = Good, Orange = Moderate, Red = Bad).

## Future Improvements

-   Incorporate real air quality data for better accuracy.
-   Add more features (e.g., weather conditions, time of day).
-   Implement cross-validation for robust model evaluation.
-   Enhance visualization with interactive elements (e.g., Plotly).
