# EDA script for Kaggle's February Tabular Playground Series competition
# Predict continuous value 'target' for each 'id'
# 10 categorical features, 14 continuous features

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

train_data = pd.read_csv('../Datasets/train.csv')
test_data = pd.read_csv('../Datasets/test.csv')

features = ['cat0', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9',
            'cont0', 'cont1', 'cont2', 'cont3', 'cont4', 'cont5', 'cont6', 'cont7', 'cont8',
            'cont9', 'cont10', 'cont11', 'cont12', 'cont13']

cats  = ['cat0', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9']
conts = ['cont0', 'cont1', 'cont2', 'cont3', 'cont4', 'cont5', 'cont6', 'cont7', 'cont8',
         'cont9', 'cont10', 'cont11', 'cont12', 'cont13']

X = train_data[features]
y = train_data.target

X_test = test_data[features]

# Histograms of continuous features
#X.hist()
#plt.show()

# Histograms of categorical features
X[cats].value_counts().plot(kind='bar')

# Scatter matrix (distributions and relations between features)
#scatter_matrix(X)
#plt.show()
