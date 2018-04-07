#!/usr/bin/env python

# File information
"""
wil_multiple_linear_regression.py: First look at multiple regression of data.
"""
__author__ = "Wil Poole"
__copyright__ = "2017"
__credits__ = "Wil Poole"
__license__ = "None"
__version__ = "0.1"
__maintainer__ = "Wil Poole"
__email__ = "@"
__status__ = "Development"


# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from os import path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Variables
data_directory = "."
data_file = "50_Startups.csv"

# Import the data
data_set = pd.read_csv(path.join(data_directory, data_file))

# Print the data set
data_set.head(n=5)


# Split into dependent and independent data
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
print(X[1:4,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap - remove the first column
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print(y_pred)

# Plot comparisons
plot = plt.scatter(y_test, y_pred, color = "red")
plt.show(plot)

# Backward elination
# Package to assess the model
import statsmodels.formula.api as sm
# Need to add column of 1's to X to account for constant
X = np.append(arr = np.ones((len(X),1)).astype(int), values = X, axis = 1)
# Create new X_opt for manuplulation
X_opt = X[:,[0,1,2,3,4,5]]
# Need to create a new regressor for our new data and class
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

print(regressor_OLS.summary())

# Remove index 2 as it has the highest P value
X_opt = X[:,[0,1,3,4,5]]
# Need to create a new regressor for our new data and class
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

print(regressor_OLS.summary())

# Remove index 1 as it has the highest P value
X_opt = X[:,[0,3,4,5]]
# Need to create a new regressor for our new data and class
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

print(regressor_OLS.summary())

# Remove index 4 as it has the highest P value
X_opt = X[:,[0,3,5]]
# Need to create a new regressor for our new data and class
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

print(regressor_OLS.summary())

# Remove index 4 as it has the highest P value
X_opt = X[:,[0,3]]
# Need to create a new regressor for our new data and class
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

print(regressor_OLS.summary())


import statsmodels.formula.api as sm
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x

SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)
