__author__ = "Ben Nelsen"
import numpy as np
"""
@@ Add class level doc string here
"""

class temperatureSeries:

    def __init__(self):
        """
        @@ Module level doc string here

        Temperature Series parameters
        """

        # Initial Import Values:
        self.name = 'default'           # Station name
        self.gDates = []                # Gregorian dates for dataset
        self.jDates = []                # Julian Dates for dataset
        self.rawTemp = []               # Temperature values for corresponding time series
        self.firstDate = []             # First Julian date for the series
        self.lastDate = []              # Last Julian date for the series
        self.tempType = 'default'       # High or low temperature values

        # Calculated Series values:
        self.allData = []               # The original dataset placed into the framework of all stations
        self.rawMask = []               # The mask of boolean values for the original raw data
        self.allDataMask = []           # A mask of boolean values for the allData series
        self.currentData = []           # Actively changed dataset

    def createHigh(self, s_name, s_dates, i_dates, d_rawTemp):
        self.name = s_name
        self.gDates = s_dates
        self.jDates = i_dates
        self.rawTemp = d_rawTemp
        self.currentData = d_rawTemp
        self.tempType = 'high'
        self.findFirstandLast()

    def createLow(self, s_name, s_dates, i_dates, d_rawTemp):
        self.name = s_name
        self.gDates = s_dates
        self.jDates = i_dates
        self.rawTemp = d_rawTemp
        self.currentData = d_rawTemp
        self.tempType = 'low'
        self.findFirstandLast()

    def generateMask(self):
        pass

    def findFirstandLast(self):
        if len(self.currentData) == 0:
            self.firstDate = np.inf()
            self.lastDate = 0
        else:
            self.firstDate = self.currentData[0]
            self.lastDate = self.currentData[-1]

    def nestData(self, universalFirstDate, universalLastDate):
        frontLength = self.firstDate - universalFirstDate
        backLength = universalLastDate - self.lastDate
        self.allData = np.hstack([np.nan(1,frontLength), self.currentData, np.nan(1,backLength)])