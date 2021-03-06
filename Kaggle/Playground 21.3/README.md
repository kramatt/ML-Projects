# Kaggle Tabular Playground Series
###### March 2021
###### [Competition Link](https://www.kaggle.com/c/tabular-playground-series-mar-2021)

**Objective:** Predict a binary target value for each ID using 19 categorical and 11 continuous features.

**Scoring:** This competition evaluates accuracy using area under the ROC curve between the predicted and actual target values.

**Result:** Competition closes at the end of March, will update with final score then.

## EDA

* No missing or mismatched values in any features. No need to impute values or drop features for lack of values.
* Features have non-descriptive titles ('cat1', 'cont5', etc.). Can't use 'real-world' sense of the problem to decide which features are more or less important.

```python
print(train_data.head)
```

| id  | cat0 | cat1 | cat2 | cat3 | cat4 | cat5 | cat6 | cat7 | cat8 | cat9 | cat10 | cat11 | cat12 | cat13 | cat14 | cat15 | cat16 | cat17 | cat18 | cont0 | cont1 | cont2 | cont3 | cont4 | cont5 | cont6 | cont7 | cont8 | cont9 | cont10 |
| --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ |

## Modeling

**Selection:** 

**Tuning:** 

## Result

On the competition set, this model earned a score of **0.88324**.

The highest current score is 0.89284, and a perfect score would be 1.
