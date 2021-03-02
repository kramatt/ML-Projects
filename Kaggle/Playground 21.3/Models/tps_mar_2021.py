# Model and predictions for Kaggle's March Tabular Playground Series competition
# Predict continuous value 'target' for each 'id'
# Accuracy scored with area under ROC curve

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score
from xgboost import XGBRegressor


# Load data and separate into train/validation/test sets
train_data = pd.read_csv('../Datasets/train.csv')
test_data = pd.read_csv('../Datasets/test.csv')

features = ['cat0', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9',
            'cat10', 'cat11', 'cat12', 'cat13', 'cat14', 'cat15', 'cat16', 'cat17', 'cat18',
            'cont0', 'cont1', 'cont2', 'cont3', 'cont4', 'cont5', 'cont6', 'cont7', 'cont8',
            'cont9', 'cont10']

X = train_data[features]
y = train_data.target

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size = 0.2, random_state=0)

X_test = test_data[features]


# One-hot encode categorical data
X_train = pd.get_dummies(X_train)
X_valid = pd.get_dummies(X_valid)
X_test = pd.get_dummies(X_test)

X_train, X_valid = X_train.align(X_valid, join='left', axis=1)
X_train, X_test = X_train.align(X_test, join='left', axis=1)


# Tuning hyperparameters - helper function
def get_score(eta, X, y):
    # Inputs:
    #   eta to use for XGBoost model
    #   X array to use as model input features
    #   y array to use as model input labels
    # Returns:
    #   average roc_auc over 5 cv folds of XGBoost model
    
    model = XGBRegressor(eta=eta, random_state=0)
    scores = cross_val_score(model, X, y, cv=5, n_jobs=-1, scoring='roc_auc')
    print(eta, scores.mean())
    return scores.mean()

# Tuning parameters - define bounds
#cv_results = {}
#for i in range(10, 35, 5):
#    cv_results[i/100] = get_score(i/100, X_train, y_train)

# Tuning parameters - plot results
#plt.plot(list(cv_results.keys()), list(cv_results.values()))
#plt.xlabel('eta')
#plt.ylabel('roc_auc')
#plt.title('roc_auc for XGBoost with varying eta')
#plt.show()

# Create and fit model
model = XGBRegressor(eta=0.2, random_state=0)
model.fit(X_train, y_train)


# Make validiation predictions and calculate accuracy
valid_preds = model.predict(X_valid)
print('roc_auc:', roc_auc_score(y_valid, valid_preds))


# Make test predictions and create .csv submission
test_preds = model.predict(X_test)
output = pd.DataFrame({'id': test_data.id, 'target': test_preds})
output.to_csv('../Submissions/submission_playground_21_3.csv', index=False)
print('Submission saved!')
