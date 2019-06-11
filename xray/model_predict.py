import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os
from sklearn.metrics import accuracy_score
import pickle
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def predict(file):
    dat = pd.read_csv(file)
    return(loaded_model.predict(dat.T))


