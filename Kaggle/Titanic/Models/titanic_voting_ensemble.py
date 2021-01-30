# Predictive model for Kaggle's Titanic Competition (Averaging Ensemble Version)
# Author: Matthew Kramer

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

train_data = pd.read_csv('../Datasets/train.csv', header=0)
test_data = pd.read_csv('../Datasets/test.csv', header=0)

y = train_data['Survived']

features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

X_train, X_val, Y_train, Y_val = train_test_split(X, y, test_size=0.2, random_state=7)

# Weak estimators
models = []
models.append(('LR',    LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA',   LinearDiscriminantAnalysis()))
models.append(('KNN',   KNeighborsClassifier()))
models.append(('CART',  DecisionTreeClassifier()))
models.append(('NB',    GaussianNB()))
models.append(('SVM',   SVC(gamma='auto')))

# Build ensemble
ensemble = VotingClassifier(models, voting='hard')

ensemble.fit(X, y)
predictions = ensemble.predict(X_test)

yhat = ensemble.predict(X_val)
acc = accuracy_score(Y_val, yhat)
print('Accuracy: %.3f' % acc)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('../Submissions/vote_ensemble.csv', index=False)
print('Your submission was successfully saved!')
