import unittest
from pandas import Series
from GetPriceData import getPriceData
from datetime import datetime

class Test_getPriceData(unittest.TestCase):
    def test_noTicker(self):
        ticker = '123'
        startDate = datetime(2013,1,1)
        data = getPriceData(ticker, startDate)
        assert data == None


    def test_noDate(self):
        ticker = 'sbux'
        startDate = ''
        data = getPriceData(ticker, startDate)
        assert data == None


    def test_getPriceData_type(self):
        ticker = 'sbux'
        startDate = datetime(2013,1,1)
        data = getPriceData(ticker, startDate)
        assert str(type(data)) == "<class 'pandas.core.frame.DataFrame'>"


    def test_getPriceData(self):
        ticker = 'sbux'
        startDate = datetime(2013,1,1)
        data = getPriceData(ticker, startDate)
        expectRaw = {'Adj Close':Series('54.79', index=datetime(2013,1,2)),
                     'Ticker':Series('sbux', index=datetime(2013,1,2))}
        expectData = DataFrame(expectRaw)
        assert data == expectData

if __name__ == '__main__':
    unittest.main()
