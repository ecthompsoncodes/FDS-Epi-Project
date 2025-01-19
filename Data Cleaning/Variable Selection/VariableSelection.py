#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:15:57 2024

@author: lizzithompson
"""

from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

analysis_data = pd.read_csv("data_all.csv")

# Load your data into X (features) and y (target) variables
X = analysis_data.iloc[:, 19].values.reshape(-1, 1)

# y is everything else
y = analysis_data.drop(analysis_data.columns[19], axis=1)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Lasso regression model
# You can adjust the alpha parameter to control the amount of regularization (default is 1.0)
lasso = Lasso(alpha=1.0)

# Fit the model to the training data
lasso.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lasso.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

# Print the mean squared error
print(f'Mean Squared Error: {mse}')

# To access the model's coefficients and intercept:
coefficients = lasso.coef_
intercept = lasso.intercept_
print(f'Coefficients: {coefficients}')
print(f'Intercept: {intercept}')
