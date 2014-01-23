'''
This file stores common functions for other modules to use

'''

#########################################################################
# List of variables
#########################################################################
STOCK_FILE_DIR = "C:/Users/glau/Downloads/stockSpreadsheets/"
CRITERIA_FILE_DIR = STOCK_FILE_DIR + "criteria/"
ERROR_FILE_DIR = STOCK_FILE_DIR + "error/"
TICKER_FILE_DIR = STOCK_FILE_DIR + "ticker/"
FINANCIAL_FILE_DIR = STOCK_FILE_DIR + "financial/"

OUTPUT_FILENAME = "allTickers.csv"

TICKER_FILENAME_AMEX = "amexTickers.csv" # Estimated run time: 1:31:42.274568 Actual run time: 1:37:34.548439 Actual run time: 1:35:53.824407
TICKER_FILENAME_NYSE = "nyseTickers.csv" # Estimated run time: 10:49:53.088216 Actual run time: 11:47:11.236284
TICKER_FILENAME_NASDAQ = "nasdaqTickers.csv" # Estimated run time: 9:58:41.077460 Actual run time: 10:11:07.569536
TICKER_FILENAME_ALL = "allTickers.csv"

TICKER_FILENAME_DEFAULT = "amexTickers.csv"
#########################################################################
# List of functions
#########################################################################

# Opens file and prints column
def get_col(filename, col):
    #print(filename)
    from csv import reader
    for row in reader(open(filename), delimiter=','):
        #print(row)
        yield row[col]
    return

# Get column "Symbol"
def get_col_symbol(filename):
    tmpList = list(get_col(filename, 0))
    return tmpList

# Get ticker from list
def get_ticker_from_list(theList):
    tickerSym = theList.pop()
    return tickerSym

# Read cells from csv file
def access_cells(ticker, statementType, reportType, fileDir):
    data = []
    from csv import reader
    for row in reader(open(fileDir + ticker + ' ' + statementType + ' ' + reportType + '.csv', 'r'), delimiter=','):
        data.append(row)
    return data

# Empties a list
def empty_the_list(theList):
    del theList[:]
    return

# Converts inputList into dataStr to write to csv
def convert_inputList_into_dataStr(theList):
    # rows contains the list of lists
    lines = []
    for row in theList:
        lines.append(','.join(map(str, row)))
        dataStr = '\n'.join(lines)
    return dataStr

# Converts errorList into dataStr to write
def convert_errorList_into_dataStr(theList):
    lines = []
    for row in theList:
        lines.append(''.join(map(str, row)))
        dataStr = '\n'.join(lines)
    return dataStr

# Open downloaded file and read file into string
def open_file(filename):
    with open(filename) as myfile:
        data = myfile.read()
    return data

# Write parsed string into a new csv file
def write_file(dataStr, filename):
    # Write dataStr to a new file
    target = open(filename, 'w')
    target.write(dataStr)
    target.close
    return

# Delete a file
def delete_file(filename):
    from os import remove
    try:
        remove(filename)
    except OSError:
        pass
    return

# Appends onto errorList tickers with no financial data and returns 'error' on ticker
# (I manually verified whether there were any financial data)
def unable_to_find_financial_data(ticker, errorList):
    errorList.append(["As of 2014-01-10, unable to find financial data on " + ticker])
    ticker = 'error'
    return ticker

# Error checks the ticker
def error_check_the_ticker(ticker, errorList):
    if 'TRC/WS' in ticker:
        ticker = unable_to_find_financial_data(ticker, errorList)
    elif 'PCG^' in ticker:
        ticker = unable_to_find_financial_data(ticker, errorList)
    elif 'GRH^' in ticker:
        ticker = unable_to_find_financial_data(ticker, errorList)
    elif '$' in ticker:
        ticker = unable_to_find_financial_data(ticker, errorList)
    elif '/' in ticker:
        tmpStr = ''.join(ticker)
        tmpStr = tmpStr.replace('/', '.')
        ticker = tmpStr
    return ticker

# Estimates the time left to run
def estimated_time_left(index, tmpInt, numSec):

    from datetime import timedelta
    floatOfNumSec = timedelta(seconds=float(numSec))
    print('Single run time: ' + str(floatOfNumSec))

    numLeft = number_of_elements_left_in_list(index, tmpInt)
    estimatedTimeLeft = numLeft * floatOfNumSec
    print('Estimated time left: ' + str(estimatedTimeLeft))
    return

# Returns number of elements left in the list
def number_of_elements_left_in_list(index, lengthOfList):
    numLeftInList = lengthOfList - index
    return numLeftInList

# Check if there are any system arguments. If there are, raise ValueError
def error_check_system_arg(sysArgv):
    if len(sysArgv) > 1:
        raise ValueError
    return

# Check if there exist any system arugments.
# If there are no arguments, assign a default to sys.argv[1]
def check_if_there_exist_any_system_argument(sysArgv):
    if len(sysArgv) < 1:
        tickerFilename = TICKER_FILENAME_DEFAULT
    else:
        tickerFilename = sysArgv[1]
    return tickerFilename

# Checks which exchange user wants to get info from. This function exists to cut down running time.
def check_which_exchange_user_wants_to_get_info_from():

    print("Which exchange to get info from?")
    print("Type '1' for amex")
    print("Type '2' for nyse")
    print("Type '3' for nasdaq")
    print("Type '4' for all")
    tickerFilename = input("Answer: ")

    if tickerFilename == '1':
        print("User picked amex")
        tickerFilename = TICKER_FILENAME_AMEX
    elif tickerFilename == '2':
        print("User picked nyse")
        tickerFilename = TICKER_FILENAME_NYSE
    elif tickerFilename == '3':
        print("User picked nasdaq")
        tickerFilename = TICKER_FILENAME_NYSE
    elif tickerFilename == '4':
        print("User picked all")
        tickerFilename = TICKER_FILENAME_ALL
    else:
        print("User input error. Default to " + TICKER_FILENAME_DEFAULT)
        tickerFilename = TICKER_FILENAME_DEFAULT
    return tickerFilename

# Checks if user just wants to get last price only. This function exists to cut down running time.
# User gets prompted with a Y/N question. This function returns true and false
def check_if_user_wants_to_download_last_price_only():
    boolAnswer = input("Download Last Price only? (Y/N): ")
    boolAnswer = boolAnswer.lower()
    if boolAnswer in 'y':
        boolAnswer = True
    elif boolAnswer in 'n':
        boolAnswer = False
    else:
        boolAnswer = True
    return boolAnswer