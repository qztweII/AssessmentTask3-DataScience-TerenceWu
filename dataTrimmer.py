import pandas as pd

oldDF = pd.read_csv("big-mac-source-data-v2.csv")

df = oldDF.drop(columns=["iso_a3", "currency_code", "dollar_ex", "GDP_local", "local_price"])
#Take out the irrelevant bits

for i in range(len(df['date'])):
    df.at[i, 'date'] = str(df.at[i, 'date'])[:4]
    df.at[i, 'date'] = int(df.at[i, 'date'])
    #Only include the year

df.sort_values(by="name")

pd.DataFrame(df)
df.to_csv("bigMacData.csv", index=False)
print("Data frame trimmed!")