# Flight Data Analysis and Prediction

This Jupyter Notebook focuses on the analysis and prediction of flight data using pandas, scikit-learn and machine learning techniques to performs analysis on flight data and applies a Random Forest model for regression tasks.

## Data Loading and Exploration

The script begins by loading the flight data from 'flightdata.csv' into a Pandas DataFrame. It provides insights into the basic information, shape, and missing values of the original DataFrame.

## Data Imputation

To handle missing values, the script utilizes a SimpleImputer from scikit-learn, replacing missing values in specified columns with the most frequent values.

## Splitting Data for Prediction

The dataset is split into features (X) and the target variable (y), which is 'arr_time' in this case. The data is further divided into training and testing sets using the train_test_split function.

## Exploratory Data Analysis

The script examines unique values, data types, and missing values in both the features and target variable. It provides an overview of the dataset's characteristics.

## Handling Missing Values and Data Transformation

Remaining missing values are dropped, and 'object' columns are converted to numerical values. The features are scaled using StandardScaler, and one-hot encoding is applied.

## Random Forest Regression

A Random Forest model is created using a pipeline with StandardScaler and RandomForestRegressor. Cross-validation scores for R^2 are computed.

Feel free to explore the script for detailed analysis and implementation details.
