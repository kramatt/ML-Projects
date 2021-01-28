# Model selection and evaluation for Titanic Competition
# Author: Matthew Kramer

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

pd.options.display.width = 0

data = pd.read_csv('../Datasets/train.csv', header=0)

#pd.plotting.scatter_matrix(train_data)
#plt.show()

y = data['Survived']

features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
X = pd.get_dummies(data[features])

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=7)

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X_train, Y_train)
