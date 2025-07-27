from pandas import *
rawdf = read_csv(Placeholder.csv)

sorteddf = rawdf.sort_values(by=Something)

cleandf = sorteddf.dropna()

cleandf.to_csv("cleaned_data.csv")