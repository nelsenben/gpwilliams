
import numpy as np

def importTemperatureFolder():
    pass

def importTemperatureFile():
    pass

def generatePseudoDates(i_startDate, i_dataLength):
    """

    i_startDate: The date the data for a station starts at
    i_dataLength: The length of data that a station has

    return: an array of dates that gives the julian date to which a data point is associated

    """
    ia_startDate = np.ones(1,i_dataLength)*i_startDate
    ia_date = np.array[range(0,i_dataLength-1)]
    ia_date = ia_date + ia_startDate
    return ia_date



print("hello world")
