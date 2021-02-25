# Kaggle Tabular Playground Series
###### February 2021
###### [Competition Link](https://www.kaggle.com/c/tabular-playground-series-feb-2021)

**Objective:** Predict a real, continuous target value for each ID using 10 categorical and 14 continuous features.

**Scoring:** This competition evaluates accuracy using RMSE.

**Result:** Competition closes at the end of February, will update with final score then.

## EDA

* No missing or mismatched values in any features. No need to impute values or drop features for lack of values.
* Features have non-descriptive titles ('cat1', 'cont5', etc.). Can't use 'real-world' sense of the problem to decide which features are more or less important.
* The most frequent values in cat0, cat2, cat4, cat6, and cat7 are present in at least 89% of the training examples. There *may* be a low correlation between these features and the target values.
* cont4 has a huge spike in frequency of values between 0.27 and 0.29. Will explore exclusion of this feature.
* Most continuous features are not normally distributed, but the target values are. Not sure what conclusion to draw from this, but it is interesting.

## Modeling

**Selection:** I chose to use an XGBoost regressor for this problem. I recently worked through some of Kaggle's mini-courses that used XGBoost,
and I wanted to get some more experience with it. I also wanted to try limiting myself to a single model, and do as best I can with that.

**Tuning:** I chose to first tune the number of estimators, *n_estimators*, and the learning rate, *eta*.
These are noted as two key hyperparameters in the XGBoost documentation.

The models were trained and evaluated with an 80/20 train/test split, a 3-fold cross-validation, and RMSE scoring.

* *n_estimators*
  * RMSE for n_estimators from 50 to 400 in steps of 50: <a href="url"><img src="https://raw.githubusercontent.com/krmatt/ML-Projects/master/Kaggle/Playground%2021.2/Models/XGB%20n_estimators%2050_450_50.png" align="center" height="360" width="480" ></a>

  * No minimum in this range. Need to use lower values for *n_estimators*.

  * RMSE for n_estimators from 10 to 50 in steps of 10: <a href="url"><img src="https://raw.githubusercontent.com/krmatt/ML-Projects/master/Kaggle/Playground%2021.2/Models/XGB%20n_estimators%2010_60_10.png" align="center" height="360" width="480" ></a>
  
  * **Best *n_estimators* value: 50**

* *eta*
  
  * RMSE for eta from 0.10 to 0.25 in steps of 0.05: <a href="url"><img src="https://raw.githubusercontent.com/krmatt/ML-Projects/master/Kaggle/Playground%2021.2/Models/XGB%20eta%200.10_0.30_0.05.png" align="center" height="360" width="480" ></a>
  
  * **Best *eta* value: 0.2**

## Result

On the competition set, this model earned a score of **0.84825**.

The highest current score is 0.84100, and a perfect score would be 1.
