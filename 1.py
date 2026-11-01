
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
df = pd.read_csv("Datasets/1-uber.csv")

# Preprocessing
df = df.dropna()
df = df[df["fare_amount"] > 0]
df = df[df["passenger_count"] > 0]

# Calculate distance
df["distance"] = np.sqrt(
    (df["pickup_latitude"] - df["dropoff_latitude"])**2 +
    (df["pickup_longitude"] - df["dropoff_longitude"])**2
)

# Remove outliers
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

df = df[df["fare_amount"].between(Q1-1.5*IQR, Q3+1.5*IQR)]

# Correlation
print(df.corr(numeric_only=True))

# Input and output
X = df[["distance", "passenger_count"]]
y = df["fare_amount"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
p1 = lr.predict(X_test)

# Random Forest
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
p2 = rf.predict(X_test)

# Evaluation
print("LR R2:", r2_score(y_test, p1))
print("LR RMSE:", np.sqrt(mean_squared_error(y_test, p1)))

print("RF R2:", r2_score(y_test, p2))
print("RF RMSE:", np.sqrt(mean_squared_error(y_test, p2)))
