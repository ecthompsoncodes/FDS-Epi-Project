# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:01:09 2024

Decision Tree Attempt

@author: scott
"""
import pandas as pd
import os as os

fileloc = "C:\\Users\\scott\\OneDrive\\Documents\\FDS 510\\Dataset"
os.chdir(fileloc)

df = pd.read_csv('resultdat.csv')

df = df.drop(df.columns[[0,5,12, 13, 14]], axis = 1)

from sklearn.model_selection import train_test_split

X = df.drop('hotspot_prop', axis = 1)
y = df['hotspot_prop']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state = 42)

model.fit(X_train, y_train)


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared:", r2)


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plot_tree(model, filled=True, feature_names=X.columns)
plt.show()