# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:04:10 2024

@author: Heather

References:
    https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron
    https://www.geeksforgeeks.org/sklearn-perceptron/
"""

import os as os

fileloc = "C:\\Users\\bowmahea\\OneDrive\\FDS Masters\\FDS 510\\epiProject"
os.chdir(fileloc)

# Dataset loading
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

#Load dataset for analysis after cleaning and combining
analysis_data = pd.read_csv("analysis_data_small.csv").values

#Split the dataset into training and testing sets
#For X, use features in column indexes 2-5; y is the last column
X, y = analysis_data[:, 6:7], analysis_data[:, 7]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)


y = y.astype('bool')
y_train = y_train.astype('bool')
y_test = y_test.astype('bool')

# Create a Perceptron classifier
perceptron = Perceptron(max_iter=100, eta0=0.1, random_state=42, verbose=1)

# Fit the model to the data
perceptron.fit(X_train, y_train)
 
#Making prediction on test data 
y_pred = perceptron.predict(X_test)

#Finding accuracy 
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}') 

# Generate a classification report 
class_report = classification_report(y_test, y_pred,)
print("Classification Report:\n", class_report) 