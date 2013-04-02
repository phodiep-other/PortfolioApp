from pandas.io.data import DataReader
from datetime import datetime

def getPriceData(ticker,source,startDate):
    """returns Price Data for ticker as pandas.DataFrame
    Date, Open, High, Low, Close, Volume, Adj Close
    
    """
    
    try:
        priceData = DataReader(ticker, source, startDate)
        priceData.pop('Open')
        priceData.pop('High')
        priceData.pop('Low')
        priceData.pop('Close')
        priceData.pop('Volume')
        priceData['Ticker'] = ticker
        priceData['Activity'] = ''
        
        return priceData
    except:
        return "Not Found"


