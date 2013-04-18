import unittest
from pandas import DataFrame

from csv_handler import import_dataFrame, export_dataFrame

class Test_csvHandler(unittest.TestCase):
    def test_noImport(self):
        data = import_dataFrame('')
        assert data == None

    def test_emptyImportExport(self):
        tempFile = 'temp.csv'
        tempExport = DataFrame()
        
        export_dataFrame(tempExport,tempFile)
        tempImport = import_dataFrame(tempFile)
        assert tempImport.empty == tempExport.empty

##    def test_importexport(self):
##        tempFile = 'temp.csv'
##        tempExport = DataFrame(['a'],[1])
##        
##        export_dataFrame(tempExport,tempFile)
##        tempImport = import_dataFrame(tempFile)
##        assert tempImport == tempExport
##        #no working, no bool for dataframe?
