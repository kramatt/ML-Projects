# Predictive model for FSAE Acceleration Times
# Author: Matthew Kramer

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

data = pd.read_csv
