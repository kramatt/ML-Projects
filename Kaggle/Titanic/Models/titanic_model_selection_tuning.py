# Model selection and evaluation for Titanic Competition
# Author: Matthew Kramer

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
#from sklearn.ensemble import RandomForestClassifier
#pd.options.display.width = 0

data = pd.read_csv('../Datasets/train.csv', header=0)

#pd.plotting.scatter_matrix(train_data)
#plt.show()

# Split data, get binary dummies
y = data['Survived']
features = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
X = pd.get_dummies(data[features])

# Split data into train/test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# Models to spot check
models = []
models.append(('LR',    LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA',   LinearDiscriminantAnalysis()))
models.append(('KNN',   KNeighborsClassifier()))
models.append(('CART',  DecisionTreeClassifier()))
models.append(('NB',    GaussianNB()))
models.append(('SVM',   SVC(gamma='auto')))

# Evaluate models
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Plot results
plt.boxplot(results, labels=names)
plt.title('Classifier Spot Check Comparison')
plt.savefig('classifier_comparison.pdf')
plt.show()
