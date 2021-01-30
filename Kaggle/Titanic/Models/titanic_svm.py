# Predictive model for Kaggle's Titanic Competition (SVM Version)
# Author: Matthew Kramer

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

train_data = pd.read_csv('../Datasets/train.csv', header=0)
test_data = pd.read_csv('../Datasets/test.csv', header=0)

y = train_data['Survived']

features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

X_train, X_val, Y_train, Y_val = train_test_split(X, y, test_size=0.2, random_state=1)

model = SVC(gamma='auto')
model.fit(X, y)
predictions = model.predict(X_test)

yhat = model.predict(X_val)
acc = accuracy_score(Y_val, yhat)
print('Accuracy: %.3f' % acc)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('../Submissions/svm.csv', index=False)
print('Your submission was successfully saved!')
