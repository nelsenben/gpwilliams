
import numpy as np
import os
import datetime
import astropy.time

def importTemperatureFolder(s_folderPath):
    pass

def importTemperatureFile(s_folderPath, s_fileName):
    s_date = []
    d_lowTemp = []
    d_highTemp = []

    s_filePath = os.path.join(s_folderPath, s_fileName)
    f_data = file(s_filePath,'r')
    for line in f_data:
        columns = line.split(' ')
        s_date.append(columns[0])
        d_lowTemp.append(float(columns[1]))
        d_highTemp.append(float(columns[2]))

    print('Debug')

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

def convertJulian(s_date, s_format):
    it_dateTimeObject = datetime.datetime.strptime(s_date, s_format)
    time = astropy.time.Time(it_dateTimeObject)
    i_julian = int(time.jd)

    return i_julian
