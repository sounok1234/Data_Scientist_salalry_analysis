import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from kmodes.kprototypes import KPrototypes
import pickle

dataset = pd.read_csv('model_data.csv')

matrix = dataset.to_numpy()

kproto = KPrototypes(n_clusters=5, init='Cao')
kproto.fit_predict(matrix, categorical=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

pickle.dump(kproto,open('model.pkl','wb+'))