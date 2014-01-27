'''
This file will extrapolate necessary data of tickers from fundamental data
Imports functions from module common_lib.py

#########################################################################
The MIT License (MIT)

Copyright (c) 2014 Gary Lau

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
#########################################################################
'''

import common_lib

inputList = [['default', 0]]
finalList = [['final default', 0]]
errorList = [['error default']]

# This class is created to get around calling "totalNumberOfSharesVal" as a global variable.
class TotalNumberOfSharesGlobalClass:
    totalNumberOfSharesVal = 'n/a'

class LastPriceClass:
    lastPriceVal = 'n/a'

class choiceExchangeClass:
    choiceExchange = common_lib.TICKER_FILENAME_DEFAULT

# Turn all string in readList into lower case for string matching purposes.
def turn_string_in_readList_into_lower_case(readList):
    for i in range(len(readList)):
        readList[i] = [x.lower() for x in readList[i]]
    return readList

# Finds the first string from the list and append to a new list
def read_from_list_append_to_new_list(tmpStr, readList):
    for i in range(len(readList)):
        if any(tmpStr in s for s in readList[i]):
            #print("true")
            j = len(readList[i])-1
            inputList.append([readList[i][0], readList[i][j]])
            value = readList[i][j]
            break
        else:
            value = 'error'
    return value

# Return the percentage value of <Argument> / last price
def last_price_to_value_percentage(value):
    value =  float(value) / float(LastPriceClass.lastPriceVal)
    value = '{percent:.4%}'.format(percent=value)
    return value

# Get the Last Price from a list
def glean_info_from_ticker_Last_Price_Now(ticker, readList):
#    print('in glean_info_from_ticker_Last_Price_Now')
    # Get Last Price
    LastPriceClass.lastPriceVal = readList[0]
    # Changes from list into a string. It's done to prevent a list in a list.
    LastPriceClass.lastPriceVal = (''.join(LastPriceClass.lastPriceVal))
    # Stores stings into a list.
    inputList.append(['last price', LastPriceClass.lastPriceVal])
    return

# Get relevant info from Balance Quarterly csv
def glean_info_from_ticker_Balance_Quarterly(ticker, readList):
#    print('in glean_info_from_ticker_Balance_Quarterly')
    #print(readList)

    # Get Date
    tmpStr = 'fiscal year'
    read_from_list_append_to_new_list(tmpStr, readList)

    # Get Book Value
    # Total Equity / Number of shares
    tmpStr = "total stockholders' equity"
    totalStockholdersEquityVal = read_from_list_append_to_new_list(tmpStr, readList)
    tmpStr = 'preferred stock'
    preferredStockVal = read_from_list_append_to_new_list(tmpStr, readList)
#    print(preferredStockVal.isdigit())
    tmpStr = 'common stock'
    commonStockVal = read_from_list_append_to_new_list(tmpStr, readList)

    # Error check
    if preferredStockVal == 'error':
        TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal = float(commonStockVal)
    else:
        # Convert strings to float for addition
        TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal = float(preferredStockVal) + float(commonStockVal)
    inputList.append(['total shares', TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal])

    if totalStockholdersEquityVal == 'error':
        bookValueVal = 'error'
    else:
        bookValueVal = float(totalStockholdersEquityVal) / float(TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal)
    inputList.append(['book value', bookValueVal])

    # Book Value / Last Price in percentage
    lastPricePercentageVal = last_price_to_value_percentage(bookValueVal)
    inputList.append((['percentage of last price to book value', lastPricePercentageVal]))

    # Get Current Ratio
    # Current Assets / Current Liabilities
    tmpStr = 'total current assets'
    totalCurrentAssetsVal = read_from_list_append_to_new_list(tmpStr, readList)
    tmpStr = 'total current liabilities'
    totalCurrentLiabilitiesVal = read_from_list_append_to_new_list(tmpStr, readList)
    read_from_list_append_to_new_list(tmpStr, readList)

    if totalCurrentLiabilitiesVal == 'error':
        currentRatioVal = 'error'
    elif totalCurrentAssetsVal == 'error':
        currentRatioVal = 'error'
    else:
        currentRatioVal = float(totalCurrentAssetsVal) / float(totalCurrentLiabilitiesVal)
    inputList.append(['current ratio', currentRatioVal])

    # Get Debt to Equity
    # Total Liabilities / Total Equity
    tmpStr = 'total liabilities'
    totalLiabilitiesVal = read_from_list_append_to_new_list(tmpStr, readList)

    if totalLiabilitiesVal == 'error':
        debtToEquityVal = 'error'
    else:
        debtToEquityVal = float(totalLiabilitiesVal) / float(totalStockholdersEquityVal)
    inputList.append(['debt to equity', debtToEquityVal])

    # Get Working Capital per sh
    # ( Current Assets - Current Liabilities ) / num of sh
    if totalCurrentAssetsVal == 'error':
        workingCaptialPerShareVal = 'error'
    elif totalCurrentLiabilitiesVal == 'error':
        workingCaptialPerShareVal = 'error'
    else:
        workingCaptialPerShareVal = ( float(totalCurrentAssetsVal) - float(totalCurrentLiabilitiesVal) ) / float(TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal)
    inputList.append(['working capital per share', workingCaptialPerShareVal])

    # Working Capital per sh / Last Price in percentage
    lastPricePercentageVal = last_price_to_value_percentage(workingCaptialPerShareVal)
    inputList.append(['percentage of last price to working capital per share', lastPricePercentageVal])

    return

# Get relevant info from Income Quarterly csv
def glean_info_from_ticker_Income_Quarterly(ticker, readList):
#    print('in glean_info_from_ticker_Income_Quarterly')

    # Get Revenue Per Share
    # revenue / num of sh
    tmpStr = 'revenue'
    revenueVal = read_from_list_append_to_new_list(tmpStr, readList)

    if revenueVal == 'error':
        revenuePerShareVal = 'error'
    else:
        revenuePerShareVal = float(revenueVal) / float(TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal)
    inputList.append(['revenue per share', revenuePerShareVal])

    # Revenue per sh / Last Price in percentage
    lastPricePercentageVal = last_price_to_value_percentage(revenuePerShareVal)
    inputList.append(['percentage of last price to revenue per share', lastPricePercentageVal])

    # Get Gross Profit Per Share
    # gross profit / num of sh
    tmpStr = 'gross profit'
    grossProfitVal = read_from_list_append_to_new_list(tmpStr, readList)

    if grossProfitVal == 'error':
        grossProfitPerShareVal = 'error'
    else:
        grossProfitPerShareVal = float(grossProfitVal) / float(TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal)
    inputList.append(['gross profit per share', grossProfitPerShareVal])

    # gross profit per sh / Last Price in percentage
    lastPricePercentageVal = last_price_to_value_percentage(grossProfitPerShareVal)
    inputList.append(['percentage of last price to gross profit per share', lastPricePercentageVal])

    # Operating Income Per Share
    # operating income / num of sh
    tmpStr = 'operating income'
    operatingIncomeVal = read_from_list_append_to_new_list(tmpStr, readList)

    if operatingIncomeVal == 'error':
        operatingIncomePerShareVal = 'error'
    else:
        operatingIncomePerShareVal = float(operatingIncomeVal) / float(TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal)
    inputList.append(['operating income per share', operatingIncomePerShareVal])

    # operating income per share / Last Price in percentage
    lastPricePercentageVal = last_price_to_value_percentage(operatingIncomePerShareVal)
    inputList.append(['percentage of last price to operating income per share', lastPricePercentageVal])

    return

# Get relevant info from Cashflow Quarterly csv
def glean_info_from_ticker_Cashflow_Quarterly(ticker, readList):
#    print('in glean_info_from_ticker_Cashflow_Quarterly')

    # Cashflow From Operating Activities per Share
    # cffoa / num of sh
    tmpStr = 'net cash provided by operating activities'
    netCashProvidedByOperatingActivitiesVal = read_from_list_append_to_new_list(tmpStr, readList)

    if netCashProvidedByOperatingActivitiesVal == 'error':
        netCashProvidedByOperatingActivitiesVal = 'error'
    else:
        netCashProvidedByOperatingActivitiesPerShare = float(netCashProvidedByOperatingActivitiesVal) / float(TotalNumberOfSharesGlobalClass.totalNumberOfSharesVal)
    inputList.append(['net cash provided by operating activities per share', netCashProvidedByOperatingActivitiesPerShare])

    # cffoa per sh / Last Price in percentage
    lastPricePercentageVal = last_price_to_value_percentage(netCashProvidedByOperatingActivitiesPerShare)
    inputList.append(['percentage of last price to net cash provided by operating activities per share', netCashProvidedByOperatingActivitiesPerShare])

    return

# Extract information from downloaded data and evaluate with my own criteria
def implement_my_criteria(ticker):
    inputList.append(['', ''])
    inputList.append(['Ticker:', ticker])

    readList = common_lib.access_cells(ticker, "Last Price", "Now", common_lib.FINANCIAL_FILE_DIR)
    # Checks if readList is empty
    if not readList:
        inputList.append(["Empty List for Last Price Now"])
        errorList.append(ticker)
        errorList.append(["Empty List for Last Price Now"])
    else:
        readList = turn_string_in_readList_into_lower_case(readList)
        try:
            glean_info_from_ticker_Last_Price_Now(ticker, readList)
        except: # catch all errors
            print("Error on glean_info_from_ticker_Last_Price_Now. Ticker: " + ticker)
            inputList.append("Error on glean_info_from_ticker_Last_Price_Now.")
            errorList.append(ticker)
            errorList.append("Error on glean_info_from_ticker_Last_Price_Now.")

    readList = common_lib.access_cells(ticker, "Balance", "Quarterly", common_lib.FINANCIAL_FILE_DIR)
    # Checks if readList is empty
    if not readList:
        inputList.append(["Empty List for Balance Quarterly"])
        errorList.append(ticker)
        errorList.append(["Empty List for Balance Quarterly"])
    else:
        readList = turn_string_in_readList_into_lower_case(readList)
        try:
            glean_info_from_ticker_Balance_Quarterly(ticker, readList)
        except:
            print("Error on glean_info_from_ticker_Balance_Quarterly. Ticker: " + ticker)
            inputList.append("Error on glean_info_from_ticker_Balance_Quarterly.")
            errorList.append(ticker)
            errorList.append("Error on glean_info_from_ticker_Balance_Quarterly.")

    readList = common_lib.access_cells(ticker, "Income", "Quarterly", common_lib.FINANCIAL_FILE_DIR)
    # Checks if readList is empty
    if not readList:
         inputList.append(["Empty List for Income Quarterly"])
         errorList.append(ticker)
         errorList.append(["Empty List for Income Quarterly"])
    else:
        readList = turn_string_in_readList_into_lower_case(readList)
        try:
            glean_info_from_ticker_Income_Quarterly(ticker, readList)
        except:
            print("Error on glean_info_from_ticker_Income_Quarterly. Ticker: " + ticker)
            inputList.append("Error on glean_info_from_ticker_Income_Quarterly.")
            errorList.append(ticker)
            errorList.append("Error on glean_info_from_ticker_Income_Quarterly.")

    readList = common_lib.access_cells(ticker, "Cashflow", "Quarterly", common_lib.FINANCIAL_FILE_DIR)
    # Checks if readList is empty
    if not readList:
        inputList.append(["Empty List for Cashflow Quarterly"])
        errorList.append(ticker)
        errorList.append(["Empty List for Cashflow Quarterly"])
    else:
        readList = turn_string_in_readList_into_lower_case(readList)
        try:
            glean_info_from_ticker_Cashflow_Quarterly(ticker, readList)
        except:
            print("Error on glean_info_from_ticker_Cashflow_Quarterly. Ticker: " + ticker)
            inputList.append("Error on glean_info_from_ticker_Cashflow_Quarterly.")
            errorList.append(ticker)
            errorList.append("Error on glean_info_from_ticker_Cashflow_Quarterly.")

#    print_list(inputList)
    finalList.extend(inputList)

    # Empty inputList for reuse.
    common_lib.empty_the_list(inputList)
#    print('end of implement_my_criteria')

    return

# The meat of this program
def do_other_stuff(tmpList):
    ticker = common_lib.get_ticker_from_list(tmpList)
    ticker = common_lib.error_check_the_ticker(ticker, errorList)
    print(ticker)
    # Checks if ticker has problems. If it does, the for loop will continue in the next iteration.
    if 'error' == ticker:
        print('Error on ticker ' + ticker)
        errorList.append(['Error on ticker ' + ticker])
        return
    elif 'Symbol' == ticker:
        return
    #print(tmpList)

    implement_my_criteria(ticker)
    return

# Writes a list to a csv file
def write_list_to_csv(theList):
    dataStr = common_lib.convert_inputList_into_dataStr(theList)
    #print(dataStr)
    common_lib.write_file(dataStr, common_lib.CRITERIA_FILE_DIR + "my criteria.csv")
    return

# Saves errorList into a file
def save_errorList():
    dataStr = common_lib.convert_errorList_into_dataStr(errorList)
    common_lib.write_file(dataStr, common_lib.ERROR_FILE_DIR + "get_fundamental_data_3_errorList.txt")
    return

def start_doing_stuff():

    # Get ticker filename
    import sys
    choiceExchangeClass.choiceExchange = common_lib.check_if_there_exist_any_system_argument(sys.argv)

    tmpList = common_lib.get_col_symbol(common_lib.TICKER_FILE_DIR + choiceExchangeClass.choiceExchange)
#    tmpList = ['IBO']
#    print_list(tmpList)

    tmpInt = len(tmpList)
    for x in range(0, tmpInt):
        print("in get_fundamental_data_3.py")
        def new_function():
#            print('in new_function()')
            do_other_stuff(tmpList)
            return
        from timeit import timeit
        numSec = timeit(new_function, number=1)
        common_lib.estimated_time_left(x, tmpInt, numSec)

#    print_list(finalList)
    write_list_to_csv(finalList)
    save_errorList()
    return

# Prints the run time of this program
def actual_run_time():

    def new_function():
        start_doing_stuff()
        return
    from timeit import timeit
    numSec = timeit(new_function, number=1)
    from datetime import timedelta
    floatOfNumSec = timedelta(seconds=float(numSec))
    print('Actual run time on get_fundamental_data_3.py: ' + str(floatOfNumSec))
    return

def main():
    actual_run_time()
    return

main()