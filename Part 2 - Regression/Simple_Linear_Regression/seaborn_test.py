# imports
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import numpy as np

# allow plots to appear directly in the notebook
%matplotlib inline

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
data.head()


sns.pairplot(data, x_vars=['TV','radio','newspaper'], y_vars='sales', size=7, aspect=0.7, kind = 'reg')

df = sns.load_dataset("anscombe")
print df.shape

sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=90, palette="muted", size=4,
           scatter_kws={"s": 50, "alpha": 1})


lm1 = smf.ols(formula='sales ~ TV', data=data).fit()
lm1.params

feature_cols = ['TV']
X = data[feature_cols]
y = data.Sales

# instantiate and fit
lm2 = LinearRegression()
lm2.fit(X, y)

# print the coefficients
print(lm2.intercept_)
print(lm2.coef_)

X_new = pd.DataFrame({'TV': [50]})
lm1.predict(X_new)

lm2.predict(50)

sns.pairplot(data, x_vars=['TV','radio','newspaper'], y_vars='sales', size=7, aspect=0.7, kind='reg')

### STATSMODELS ###

# print the confidence intervals for the model coefficients
lm1.conf_int()

### STATSMODELS ###

# print the p-values for the model coefficients
lm1.pvalues

### SCIKIT-LEARN ###

# print the R-squared value for the model
lm2.score(X, y)
