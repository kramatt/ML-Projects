import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDRegressor
#from sklearn.linear_model import ElasticNet
#from sklearn.linear_model import Lasso
#from sklearn.linear_model import Ridge
#from sklearn.svm import SVR #try kernel=linear and kernel=rbf
from sklearn.neighbors import KNeighborsRegressor
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.ensemble import ExtraTreesRegressor
#from sklearn.ensemble import AdaBoostRegressor
#from sklearn.ensemble import GradientBoostingRegressor
#from sklearn.ensemble import VotingRegressor
#from sklearn.ensemble import StackingRegressor

# Import data and organize
file = 'Reduced Data/fsae-accel-skidpad-times-noheader.csv'
names = ['Year','Track','Car Num','Team','Country','Engine Cylinders','Engine Displacement (cc)','Weight (kg)','Weight (lbs)','Accel Best Time','Skidpad Best Time']
dataframe = pd.read_csv(file, names=names)
array = dataframe.values
X = array[:,5:9]
Ya = array[:,9]
Ys = array[:,10]
Ya = Ya.astype('float')
Ys = Ys.astype('float')

# Initialize models
models = []
models.append(('SGD', SGDRegressor()))
#models.append(('EN', ElasticNet()))
#models.append(('LS', Lasso()))
#models.append(('RD', Ridge()))
#models.append(('SVR', SVR()))
models.append(('KN', KNeighborsRegressor()))
#models.append(('RF', RandomForestRegressor()))
#models.append(('ET', ExtraTreesRegressor()))
#models.append(('AB', AdaBoostRegressor()))
#models.append(('GB', GradientBoostingRegressor()))
#models.append(('VR', VotingRegressor()))
#models.append(('SR', StackingRegressor()))

# Evaluate models
results = []
model_names = []
scoring = 'accuracy'
for name, model in models:
    kfold = KFold(n_splits=10, random_state=7, shuffle=True) # Look at changing KFold parameters
    cv_results = cross_val_score(model, X, Ya, cv=kfold, scoring=scoring)
    results.append(cv_results)
    model_names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
