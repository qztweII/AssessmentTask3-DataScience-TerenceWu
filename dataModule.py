from pandas import *
import matplotlib.pyplot as plt

df = None

def read(data):
    df = read_csv(data)
    return df

def update(data):
    global df
    df = data

def graph(data):
    plt.scatter(data["Country"], data["Price difference"])
    plt.savefig("TEST!!!!")
    
def clean(column):
    dfNoNA = df[column].dropna() #Takes out the N/A values from that one column
    median = dfNoNA.median() #Finds the median of the leftover values
    df[column] = df[column].fillna(median) #Sticks the median back into the N/A values

def everyNYears(years, n):
    #Find the years column
    #Take every n years and store seperately
    #Return the result
    pass

def combine(data1, data2, common, data1Name, data2Name):
    for col in data1.columns:
        data1.rename({col : (str(col) + data1Name)})
    for col in data2.columns:
        data2.rename({col : (str(col) + data2Name)})
    mergedData = merge(data1, data2, how='inner', on=common)
    return mergedData
