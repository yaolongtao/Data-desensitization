import pandas as pd

data = pd.read_table('data/15年体测.csv',sep=',')
print(data[0:10])
