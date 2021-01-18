import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

file = 'Reduced Data/fsae-accel-skidpad.csv'
dataframe = pd.read_csv(file)
