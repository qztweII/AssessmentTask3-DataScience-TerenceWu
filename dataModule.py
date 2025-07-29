import pandas as pd

df = None

def read(data):
    df = pd.read_csv(data)
    return df

def update(data):
    global df
    df = data

def graph():
    return df.pd.plot()
    
def clean(column):
    dfNoNA = df[column].pd.dropna() #Takes out the N/A values from that one column
    median = dfNoNA.pd.median() #Finds the median of the leftover values
    df[column] = df[column].fillna(median) #Sticks the median back into the N/A values

def everyNYears(years, n):
    #Find the years column
    #Take every n years and store seperately
    #Return the result

def combine(data1, data2, common, data1Name, data2Name):
    for col in data1.columns:
        data1.pd.rename({col : (str(col) + data1Name)})
    for col in datt2.columns:
        data2.pd.rename({col : (str(col) + data2Name)})
    mergedData = pd.merge(data1, data2, how='inner', on=common)
    return mergedData
