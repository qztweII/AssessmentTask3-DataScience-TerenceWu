import data_module as dm

df = dm.read("Dummy Data.csv")

print(df.describe)