# Predictive model for Kaggle's Titanic Competition (SVM Voting Version)
# Author: Matthew Kramer

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

train_data = pd.read_csv('../Datasets/train.csv', header=0)
test_data = pd.read_csv('../Datasets/test.csv', header=0)

y = train_data['Survived']

features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

X_train, X_val, Y_train, Y_val = train_test_split(X, y, test_size=0.2, random_state=7)

# Estimators
models = []
models.append(('SVM1',   SVC(probability=True, kernel='poly', degree=1)))
models.append(('SVM2',   SVC(probability=True, kernel='poly', degree=2)))
models.append(('SVM3',   SVC(probability=True, kernel='poly', degree=3)))
models.append(('SVM4',   SVC(probability=True, kernel='poly', degree=4)))
models.append(('SVM5',   SVC(probability=True, kernel='poly', degree=5)))

# Build ensemble
ensemble = VotingClassifier(models, voting='soft')

# Make submission predictions
ensemble.fit(X, y)
predictions = ensemble.predict(X_test)

# Evaluate estimators individually
results = []
names = []
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
for name, model in models:
    score = cross_val_score(model, X_train, Y_train, cv=cv, scoring='accuracy', n_jobs=-1, error_score='raise')
    results.append(score)
    names.append(name)
    print('%s: %f (%f)' % (name, score.mean(), score.std()))

e_score = cross_val_score(ensemble, X_train, Y_train, cv=cv, scoring='accuracy', n_jobs=-1, error_score='raise')
results.append(e_score)
names.append('SVMe')
print('%s: %f (%f)' % ('SVMe', e_score.mean(), e_score.std()))

# Create submission
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('../Submissions/svm_vote.csv', index=False)
print('Your submission was successfully saved!')

# Plot results
plt.boxplot(results, labels=names, showmeans=True)
plt.savefig('svm_degree_comparison.pdf')
plt.show()
