from pandas import *
df = read_csv("Big Mac.csv")
columnHeads = [list(df.columns.values)]
print(columnHeads)