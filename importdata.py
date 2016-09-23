__author__ = "Ben Nelsen"

import numpy as np
import os
import datetime
import astropy.time
import temperatureSeries

def importTemperatureFolder(s_folderPath):
    region = []
    for file in os.listdir(s_folderPath):
        if file.endswith(".dat"):
            lowTempSeries, highTempSeries = importTemperatureFile(s_folderPath, file)
            station = np.hstack((lowTempSeries, highTempSeries))

        region.append(station)
    print('debug')


def importTemperatureFile(s_folderPath, s_fileName):
    """
    Imports and parses a temperature file. Files must be formatted as follows:
    YYYY-MM-DD  LowTemp  HighTemp

    s_folderPath: The path that the current file resides in
    s_fileName:  The name of the current file

    return:

    """
    s_date = []
    d_lowTemp = []
    d_highTemp = []
    highTempSeries = temperatureSeries.temperatureSeries()
    lowTempSeries = temperatureSeries.temperatureSeries()

    # Join the path for the file specified and read data from the columns
    s_filePath = os.path.join(s_folderPath, s_fileName)
    f_data = file(s_filePath,'r')
    # Read dates, low, and high temperatures for a dataset
    for line in f_data:
        columns = line.split('  ')
        s_date.append(columns[0])
        d_lowTemp.append(float(columns[1]))
        d_highTemp.append(float(columns[2]))

    f_data.close()

    # Convert Gregorian dates into Julian dates
    i_dates = np.zeros(len(s_date))
    for i_index in range(0,len(s_date)):
        i_dates[i_index] = convertJulian(s_date[i_index],'%Y-%m-%d')

    highTempSeries.createHigh(s_fileName, s_date, i_dates, d_highTemp)
    lowTempSeries.createLow(s_fileName, s_date, i_dates, d_lowTemp)

    return lowTempSeries, highTempSeries

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
