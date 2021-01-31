# Predictive model for FSAE Acceleration Times
# Author: Matthew Kramer

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
#from sklearn.linear_model import SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
#from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.cross_decomposition import PLSRegression
#from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

# Load data
data = pd.read_csv('Reduced Data/fsae-accel-skidpad-times.csv', header=0)

# Peek at data
#print(data.head())
#print(data.describe())
#print(data.nunique())

# Set I/D variables
y = data['Accel Best Time']

features=['Engine Cylinders', 'Engine Displacement (cc)', 'Weight (lbs)']
X = pd.get_dummies(data[features])

print(y.head())
print(X.head())


# Train test split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# Models to evaluate
models = []
models.append(('Ridge', Ridge()))
#models.append(('SGD',   SGDRegressor()))
models.append(('KNN',   KNeighborsRegressor()))
#models.append(('GP',    GaussianProcessRegressor()))
models.append(('PLS',   PLSRegression()))
#models.append(('Tree',  DecisionTreeRegressor()))
models.append(('SVM',   SVR()))

# Evaluate models
results = []
names = []
for name, model in models:
    cv = KFold(n_splits=10, random_state=1, shuffle=True)
    score = cross_val_score(model, X_train, Y_train, cv=cv, scoring='r2')
    results.append(score)
    names.append(name)
    print('%s: %f (%f)' % (name, score.mean(), score.std()))

# Plot results
plt.boxplot(results, labels=names, showmeans=True)
#plt.savefig('Figures/accel_model_comparison.pdf')
plt.show()
