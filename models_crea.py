# -*- coding: utf-8 -*-
"""models_crea.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12SzdnHuKKulwqBRUNHGKl4YI_l3mZE2a
"""

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('Housing.csv')
features = dataset.drop('price', axis=1)
target = dataset['price']

categorical_cols = features.select_dtypes(include=['object']).columns.tolist()
print("Categorical columns in the dataset:", categorical_cols)

features_encoded = pd.get_dummies(features, columns=categorical_cols)
print("Features after one-hot encoding:", features_encoded.columns.tolist())

X_train, X_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.2, random_state=42)
rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X_train, y_train)

predictions_rf = rf_regressor.predict(X_test)
mse_rf = mean_squared_error(y_test, predictions_rf)
print("Random Forest Regressor Mean Squared Error:", mse_rf)

with open('random_forest_regressor_model.pkl', 'wb') as file:
    pickle.dump(rf_regressor, file)

svr_regressor = SVR()
svr_regressor.fit(X_train, y_train)
predictions_svr = svr_regressor.predict(X_test)
mse_svr = mean_squared_error(y_test, predictions_svr)
print("SVR Mean Squared Error:", mse_svr)

with open('svr_model.pkl', 'wb') as file:
    pickle.dump(svr_regressor, file)

linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)
predictions_linear = linear_regressor.predict(X_test)
mse_linear = mean_squared_error(y_test, predictions_linear)
print("Linear Regression Mean Squared Error:", mse_linear)

with open('linear_regression_model.pkl', 'wb') as file:
    pickle.dump(linear_regressor, file)