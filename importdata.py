__author__ = "Ben Nelsen"

import numpy as np
import os
import datetime
import astropy.time
import temperatureSeries
import parameters

def importTemperatureFolder(s_folderPath):
    region = []
    for file in os.listdir(s_folderPath):
        if file.endswith(".dat"):
            lowTempSeries, highTempSeries = importTemperatureFile(s_folderPath, file)
            if lowTempSeries == 0 and highTempSeries == 0:
                pass
            else:
                if len(region) == 0:
                    i_firstDate = min(lowTempSeries.firstDate, highTempSeries.firstDate)
                    i_lastDate = max(lowTempSeries.lastDate, lowTempSeries.lastDate)
                else:
                    i_firstDate = min(lowTempSeries.firstDate, highTempSeries.firstDate, i_firstDate)
                    i_lastDate = max(lowTempSeries.lastDate, lowTempSeries.lastDate, i_lastDate)
                station = np.hstack((lowTempSeries, highTempSeries))
                region.append(station)
    print('debug')
    for station in region:
        for temperature in station:
            temperature.nestData()
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

    # Slice out data only between start and end. Eventually al data will be extended to the extents of the largest dataset
    # however, for now we want to trim any fat from the dateset
    i_lowStart, i_lowStop, i_lowDatesPresent, i_lowDatesMissing = findValues(d_lowTemp)
    s_lowDates = s_date[i_lowStart:i_lowStop]
    d_lowTemp = d_lowTemp[i_lowStart:i_lowStop]

    i_highStart, i_highStop, i_highDatesPresent, i_highDatesMissing = findValues(d_highTemp)
    s_highDates = s_date[i_highStart:i_highStop]
    d_highTemp = d_highTemp[i_highStart:i_highStop]

    if i_lowStop == 0 and i_highStop == 0:
        # There is no data here to process, so there is no reason to store it
        lowTempSeries = 0
        highTempSeries = 0

    elif i_lowDatesPresent < 50*365 and i_highDatesPresent < 50*365:
        # This restriction is currently very arbitrary. However, if less than one year of data is present not much can be done so the station should be removed.
        lowTempSeries = 0
        highTempSeries = 0

    else:
        # Convert Gregorian dates to Julian for storing in the temperature object.
        i_datesLow = np.zeros(len(s_lowDates))
        for i_index in range(0, len(s_lowDates)):
            i_datesLow[i_index] = convertJulian(s_lowDates[i_index], '%Y-%m-%d')

        i_datesHigh = np.zeros(len(s_highDates))
        for i_index in range(0, len(s_highDates)):
            i_datesHigh[i_index] = convertJulian(s_highDates[i_index], '%Y-%m-%d')

        lowTempSeries.createLow(s_fileName, s_highDates, i_datesLow, d_lowTemp)
        highTempSeries.createHigh(s_fileName, s_lowDates, i_datesHigh, d_highTemp)

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

def findValues(da_temperatureValues):
    """

    :param da_temperatureValues: temperature dataset
    :return: the beginning and ending index for found data, the amount of data present, and the amount of data missing.
                If no data is found the data should be removed
    """
    da_tempMask = np.isnan(da_temperatureValues)
    da_valueIndex = np.where(da_tempMask == 0)
    da_valueIndex = da_valueIndex[0]
    if da_valueIndex.size == 0:
        return 0, 0, 0, 0

    else:
        da_gaps = da_valueIndex[1:-1] - da_valueIndex[0:-2]
        da_gaps = da_gaps - 1
        i_dataAbsent = np.sum(da_gaps)
        i_dataPresent = da_valueIndex[-1]-da_valueIndex[0] - i_dataAbsent
        return da_valueIndex[0], da_valueIndex[-1], i_dataPresent, i_dataAbsent
