from pandas import *
import matplotlib.pyplot as plt

def sort(df, stuff, goUp):
    sortedDF = df.sort_values(by = stuff, ascending = goUp)
    return sortedDF

def graph(data, settingsAvailable):
    settingsAvailable.pop("Country")
    for i in settingsAvailable:
        if settingsAvailable[i]: #Plot according to the settings
            plt.plot(data["Country"], data[i]) #Plot the lines
    plt.ylabel("Price of Big Mac (USD)")
    plt.title("Big Mac Prices by Country")
    plt.xticks(rotation = 90)
    plt.show()
    plt.savefig("Graph - first thing") #This is not working(saves a blank figure)
    
def clean(df, subsitution):
    for i in df:
        dfNoNA = df[i].dropna() #Takes out the N/A values from that one column
        try:
            if subsitution:
                median = dfNoNA.median() #Finds the median of the leftover values
                df[i] = df[i].fillna(median) #Sticks the median back into the N/A values
        except:
            pass

def toNum(column, thingToRemove):
    for i in range(len(column)):
        thing = str(column[i])
        cleanedThing = thing.replace(thingToRemove, "")
        column[i] = float(cleanedThing)

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
