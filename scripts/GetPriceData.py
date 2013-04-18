import pandas.io.data as pd
from datetime import datetime, timedelta

def getPriceData(ticker,startDate):
    """returns Price Data for ticker as pandas.DataFrame
    Date, Open, High, Low, Close, Volume, Adj Close
    
    """
    source = 'yahoo'
    try:
        priceData = pd.DataReader(ticker, source, startDate)
        priceData.pop('Open')
        priceData.pop('High')
        priceData.pop('Low')
        priceData.pop('Close')
        priceData.pop('Volume')
        priceData['Ticker'] = ticker
        
        return priceData
    except:
        return None

def getRecentPrice(ticker):

    startDate = datetime.today() - timedelta(days=3)
    
    try:
        priceData = getPriceData(ticker,startDate)
        return priceData.tail(1)
    except:
        return None

def getDatePrice(ticker,date):
    price = getPriceData(ticker,date)
    return price.head(1)


def loop_getPrice(df):
    result = pd.DataFrame()
    try:
        for i in range(len(df)):
            temp = getRecentPrice(df['Ticker'][i])
            result = result.append(temp)
        return result
    except:
        return result
