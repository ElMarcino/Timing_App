import pandas as pd


df = pd.read_csv('Times.csv')

df.to_excel('Times.xlsx', index=None, header=True)
