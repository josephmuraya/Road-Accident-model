# -*- coding: utf-8 -*-
"""road accident model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DLailXhS54yFWAKA3koLmj1CD4PptAHB
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

joseph=pd.read_csv('/content/roadaccidents.csv')
joseph.head()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
joseph=pd.read_csv('roadaccidents.csv')
x=joseph.drop('Casualty Severity',axis=1)
y=joseph['Casualty Severity']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8,random_state=42)
regressor=LinearRegression()

regression=DecisionTreeClassifier(criterion='entropy',random_state=42)
regression.fit(x_train,y_train)

y_pred=regression.predict(x_test)
print (y_pred)

import joblib
joblib.dump(regression,'reression model.pkl')