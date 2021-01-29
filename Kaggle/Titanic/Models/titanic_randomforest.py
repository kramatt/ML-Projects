# Predictive model for Kaggle's Titanic Competition (Random Forest Version)
# Author: Matthew Kramer

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv('../Datasets/train.csv', header=0)
test_data = pd.read_csv('../Datasets/test.csv', header=0)

y = train_data['Survived']

features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('../Submissions/randomforest.csv', index=False)
print('Your submission was successfully saved!')
