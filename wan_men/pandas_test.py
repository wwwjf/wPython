import pandas as pd
import numpy as np
df = pd.read_csv('test.csv')
print(df.head())
print('--------')
print(type(df))

print('--------')
print(df[df.Sex=='male'])
print('--------')
print(df.loc[:2])