#
# Evaluate decision tree performance on train and test sets with different tree depths
#

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot

# Create dataset and prepare data
X, y = make_classification(n_samples=10000, n_features=20, n_informative=5, n_redundant=15, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create evaluation objects
train_scores, test_scores = list(), list()
values = [i for i in range(1, 21)]

# Evaluate a decision tree for each depth
for i in values:
    # configure and fit model
    model = DecisionTreeClassifier(max_depth=i)
    model.fit(X_train, y_train)
    # evaluate model on train dataset
    train_yhat = model.predict(X_train)
    train_acc = accuracy_score(y_train, train_yhat)
    train_scores.append(train_acc)
    # evaluate model on test dataset
    test_yhat = model.predict(X_test)
    test_acc = accuracy_score(y_test, test_yhat)
    test_scores.append(test_acc)
    # summarize progress
    print('>%d, train: %.3f, test: %.3f' % (i, train_acc, test_acc))

# Plot train and test performance vs tree depth
pyplot.plot(values, train_scores, '-o', label='Train')
pyplot.plot(values, test_scores, '-o', label='Test')
pyplot.legend()
pyplot.show()
