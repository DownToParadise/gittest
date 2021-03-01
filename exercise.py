import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = "ex1data2.txt"
data2 = pd.read_csv(path, header=None, names=['Size', 'Bedroom', 'Price'])
data2.head()
print(data2.head())