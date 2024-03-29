
import pandas as pd

# Load the data
df = pd.read_csv('flightdata.csv')

# Display basic information about the DataFrame
print("Original DataFrame Info:")
df.info()

# Display the shape of the original DataFrame
print("Original DataFrame Shape:", df.shape)

# Display whether there are any missing values in the original DataFrame
print("Original DataFrame Has Missing Values:", df.isnull().values.any())

# Display whether there are any missing values in the original DataFrame
print("Original DataFrame Has Missing Values:", df.isnull().values.any())

# Display the count of missing values for each column in the original DataFrame
print("Original DataFrame Missing Values per Column:")
print(df.isnull().sum())

from sklearn.impute import SimpleImputer

# Columns to impute
columns_to_impute = ['dep_time', 'dep_delay', 'arr_time', 'arr_delay', 'tailnum', 'air_time', 'avgdelay']

# Replace 'mean' with 'most_frequent' for non-numeric data
imputer = SimpleImputer(strategy='most_frequent')

# Fit and transform the imputer on the specified columns
df[columns_to_impute] = imputer.fit_transform(df[columns_to_impute])

# Display the shape and missing values of the DataFrame after dropping columns
print("\nDataFrame Info After Column imputation:")
print(df.info())

print("\nmissing values of the DataFrame after dropping columns:", df.isnull().sum())

print("\nDataFrame Shape After Column imputation:", df.shape)

df.head()

from sklearn.model_selection import train_test_split

# Specify the features (X) and the target variable (y)
X = df.drop(['arr_time'], axis=1)  # Adjust with your target variable
y = df['arr_time']  # Replace 'arrival_time' with your target variable

# Split the data into training and testing sets (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting sets
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

from sklearn.model_selection import cross_val_score, cross_val_predict, StratifiedKFold
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

print("Unique values in y_train:", y_train.unique())

# @title
print(X_train.dtypes)
print(X_train.isnull().sum())

print(y_train.dtypes)
print(y_train.isnull().sum())

# Identify unique values in columns with 'object' data type in X_train
object_columns_X = X_train.select_dtypes(include=['object']).columns
for column in object_columns_X:
    print(f"Unique values in {column}: {X_train[column].unique()}")

# Check the unique values in y_train
print("Unique values in y_train:", y_train.unique())

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline

# Check for and handle missing values
X_train = X_train.dropna()
y_train = y_train[X_train.index]  # Adjust y_train accordingly

# Convert 'object' columns to numerical values
X_train['dep_time'] = pd.to_numeric(X_train['dep_time'], errors='coerce')
X_train['dep_delay'] = pd.to_numeric(X_train['dep_delay'], errors='coerce')
X_train['arr_delay'] = pd.to_numeric(X_train['arr_delay'], errors='coerce')
X_train['air_time'] = pd.to_numeric(X_train['air_time'], errors='coerce')

# Drop remaining missing values
X_train = X_train.dropna()

# Ensure all features are numeric
X_train = pd.get_dummies(X_train)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Random Forest with pipeline
random_forest_model = make_pipeline(StandardScaler(), RandomForestRegressor())
random_forest_scores = cross_val_score(random_forest_model, X_train_scaled, y_train, cv=5, scoring='r2')

print("Random Forest Cross-Validation Scores:", random_forest_scores)
print("Random Forest Mean R^2:", random_forest_scores.mean())
