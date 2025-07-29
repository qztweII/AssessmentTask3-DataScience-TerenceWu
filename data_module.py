import pandas as pd

def read(data):
    df = pd.read_csv(data)
    return df


def update(data):
    global df
    df = data

def graph():
    df.pd.plot()

def clean(column):
    dfNoNA = df[columbn].pd.dropna() #Takes out the N/A values from that one column
    median = dfNoNA.pd.median() #Finds the median of the leftover values
    df[column] = df[column].fillna(median) #Sticks the median back into the N/A values
