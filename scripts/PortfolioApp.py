from GetPriceData import *
from csv_handler import *
import pandas as pd


def calcValue(shares,price):
    try:
        return shares * price
    except:
        return None
    
def calcTotal(dataframe):
    total = 0
    try:
        total = dataframe.sum()['Value']
        return total
    except:
        return results
    
def mergeTicker(df1,df2):
    result = pd.DataFrame()
    try:
        result = pd.merge(df1, df2, on='Ticker')
        return result
    except:
        return result

def addValueColumn(df):
    df['Value'] = calcValue(df['Shares'],df['Adj Close'])
    return df


#------Main--------------

port_file = 'portfolio.csv'


portfolio = import_dataFrame(port_file)
recentPrices = loop_getPrice(portfolio)
current = mergeTicker(portfolio, recentPrices)
current = addValueColumn(current)

print current
currentsum = calcTotal(current)
print 'Current Value = ' + str(currentsum)
