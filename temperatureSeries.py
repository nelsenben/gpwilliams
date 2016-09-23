__author__ = "Ben Nelsen"

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
        self.tempType = 'high'

    def createLow(self, s_name, s_dates, i_dates, d_rawTemp):
        self.name = s_name
        self.gDates = s_dates
        self.jDates = i_dates
        self.rawTemp = d_rawTemp
        self.tempType = 'low'