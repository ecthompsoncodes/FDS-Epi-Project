# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:58:25 2024

@author: bowmahea
"""

from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import Perceptron 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
#loading dataset 
data = load_iris() 

#Splitting the dataset to train data and test data 
X, y = data.data[:100, :], data.target[:100] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

#Making a perceptron classifier 
perceptron = Perceptron(max_iter=100, eta0=0.1, random_state=42, verbose=1) 
perceptron.fit(X_train, y_train) 

#Making prediction on test data 
y_pred = perceptron.predict(X_test) 
#Finding accuracy 
accuracy = accuracy_score(y_test, y_pred) 
print(f'Accuracy: {accuracy}') 

# Generate a classification report 
class_report = classification_report(y_test, y_pred) 
print("Classification Report:\n", class_report) 

