'''
This file will download fundamental data from the internet


This link will download 15-years of financial data for ticker FLWS:
http://www.gurufocus.com/download_dataset.php?symbol=FLWS

Annual Sheet:
Income Statement for ZBB
http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XASE:ZBB&region=usa&culture=en-US&cur=USD&reportType=is&period=12&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=859833&denominatorView=raw&number=1

Balance Sheet for ZBB
http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XASE:ZBB&region=usa&culture=en-US&cur=USD&reportType=bs&period=12&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=566211&denominatorView=raw&number=1

Cash Flow Statement for ZBB
http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XASE:ZBB&region=usa&culture=en-US&cur=USD&reportType=cf&period=12&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=114044&denominatorView=raw&number=1

Quarterly Sheet:
Income Statement for ZBB
http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XASE:ZBB&region=usa&culture=en-US&cur=USD&reportType=is&period=3&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=743877&denominatorView=raw&number=1

Balance Sheet for ZBB
http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XASE:ZBB&region=usa&culture=en-US&cur=USD&reportType=bs&period=3&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=358736&denominatorView=raw&number=1

Cashflow Statement for ZBB
http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XASE:ZBB&region=usa&culture=en-US&cur=USD&reportType=cf&period=3&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=17123&denominatorView=raw&number=1

Last stock price for ZBB (check this website for additional info - http://www.gummy-stuff.org/Yahoo-data.htm)
http://finance.yahoo.com/d/quotes.csv?s=ZBB&f=l1
'''

import urllib.request
import time
import timeit
import common_lib


inputList = [['default', 0]]
finalList = [['final default', 0]]
errorList = [['error default']]

# This class is created to get around calling "flagLastPrice" as a global variable.
class flagLastPriceClass:
    flagLastPrice = True

class choiceExchangeClass:
    choiceExchange = common_lib.TICKER_FILENAME_DEFAULT

# Get Last Price of the ticker
def get_last_price_to_csv(ticker):
    urlStr = "http://finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=l1"
#    print("Last Price for " + ticker)
    try:
        get_fin_data_from_web(urlStr, ticker, "Last Price", "Now")
    except:
        print("Error getting Last Price for " + ticker)
        errorList.append(ticker)
        errorList.append("Error getting Last Price")
    return

# Get financial data from the web and write data to a new file
def get_fin_data_from_web(urlStr, ticker, statementType, reportType):
    # Get data
    response = urllib.request.urlopen(urlStr)
    html = response.read()
    htmlStatus = response.status
#    print("in get_fin_data_from_web")
#    print(htmlStatus)

    if htmlStatus == 200:
        # Write data to a new file
        target = open(common_lib.FINANCIAL_FILE_DIR + ticker + " " + statementType + " " + reportType + ".csv", 'wb')
        target.write(html)
        target.close
    else:
        # Integer codes are at http://docs.python.org/3.3/library/http.client.html#http.client.HTTPResponse
        print("Error. htmlStatus is :" + htmlStatus)
    return

# Get Annual Income Statement of the ticker
def get_annual_income_statement_to_csv(ticker):
    urlStr = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=" + ticker + "&region=usa&culture=en-US&cur=USD&reportType=is&period=12&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=859833&denominatorView=raw&number=1"
#    print("Annual Income Statement for " + ticker)
    try:
        get_fin_data_from_web(urlStr, ticker, "Income", "Annual")
    except:
        print("Error getting Annual Income Statement for " + ticker)
        errorList.append(ticker)
        errorList.append("Error getting Annual Income Statement")
    return

# Get Annual Balance Sheet of the ticker
def get_annual_balance_sheet_to_csv(ticker):
    urlStr = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=" + ticker + "&region=usa&culture=en-US&cur=USD&reportType=bs&period=12&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=566211&denominatorView=raw&number=1"
#    print("Annual Balance Sheet for " + ticker)
    try:
        get_fin_data_from_web(urlStr, ticker, "Balance", "Annual")
    except:
        print("Error getting Annual Balance Sheet for " + ticker)
        errorList.append(ticker)
        errorList.append("Error getting Annual Balance Sheet")
    return

# Get Annual Cashflow Statement of the ticker
def get_annual_cashflow_statement_to_csv(ticker):
    urlStr = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=" + ticker + "&region=usa&culture=en-US&cur=USD&reportType=cf&period=12&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=114044&denominatorView=raw&number=1"
#    print("Annual Cash Flow Statement for " + ticker)
    try:
        get_fin_data_from_web(urlStr, ticker, "Cashflow", "Annual")
    except:
        print("Error getting Annual Cash Flow Statement for " + ticker)
        errorList.append(ticker)
        errorList.append("Error getting Annual Cash Flow Statement")
    return

# Get Quarterly Income Statement of the ticker
def get_quarterly_income_statement_to_csv(ticker):
    urlStr = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=" + ticker + "&region=usa&culture=en-US&cur=USD&reportType=is&period=3&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=743877&denominatorView=raw&number=1"
#    print("Quarterly Income Statement for " + ticker)
    try:
        get_fin_data_from_web(urlStr, ticker, "Income", "Quarterly")
    except:
        print("Error getting Quarterly Income Statement for " + ticker)
        errorList.append(ticker)
        errorList.append("Error getting Quarterly Income Statement")
    return

# Get Quarterly Balance Sheet of the ticker
def get_quarterly_balance_sheet_to_csv(ticker):
    urlStr = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=" + ticker + "&region=usa&culture=en-US&cur=USD&reportType=bs&period=3&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=358736&denominatorView=raw&number=1"
#    print("Quarterly Balance Sheet for " + ticker)
    try:
        get_fin_data_from_web(urlStr, ticker, "Balance", "Quarterly")
    except:
        print("Error getting Quarterly Balance Sheet for " + ticker)
        errorList.append(ticker)
        errorList.append("Error getting Quarterly Balance Sheet")
    return

# Get Quarterly Cashflow Statement of the ticker
def get_quarterly_cashflow_statement_to_csv(ticker):
    urlStr = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=" + ticker + "&region=usa&culture=en-US&cur=USD&reportType=cf&period=3&dataType=A&order=asc&columnYear=5&rounding=1&view=raw&r=17123&denominatorView=raw&number=1"
#    print("Quarterly Cash Flow Statement for " + ticker)
    try:
        get_fin_data_from_web(urlStr, ticker, "Cashflow", "Quarterly")
    except:
        print("Error getting Quarterly Cash Flow Statement for " + ticker)
        errorList.append(ticker)
        errorList.append("Error getting Quarterly Cash Flow Statement")
    return

# This function holds other functions for functionality purpose
def get_everything_else(ticker):
    get_annual_income_statement_to_csv(ticker)
    time.sleep(1)
    get_annual_balance_sheet_to_csv(ticker)
    time.sleep(1)
    get_annual_cashflow_statement_to_csv(ticker)
    time.sleep(1)
    get_quarterly_income_statement_to_csv(ticker)
    time.sleep(1)
    get_quarterly_balance_sheet_to_csv(ticker)
    time.sleep(1)
    get_quarterly_cashflow_statement_to_csv(ticker)
    time.sleep(1)
    return

def parse_statements(readStr):
    # Gets rid of the first row.
    startPos = readStr.find("Fiscal year")
    endPos = len(readStr)
    readStr = readStr[startPos:endPos]
    return readStr

# Get financial statements from web and convert them into csv file
def get_statements_to_csv(stockFileDir, ticker):
    #print("in get_statements_to_csv")
    if ticker != 'Symbol':
        if(flagLastPriceClass.flagLastPrice == True):
            get_last_price_to_csv(ticker)
        elif(flagLastPriceClass.flagLastPrice == False):
            get_last_price_to_csv(ticker)
            time.sleep(1)
            get_everything_else(ticker)
            # I separated get_last_price_to_csv() from get_everything_else to allow commenting out get_everything_else,
            #   because balance sheets, income statements and cashflow statements doesn't change everyday,
            #   but the last price does. It would be faster this way.

        # Parse csv files
        readStr = common_lib.open_file(stockFileDir + ticker + " " + "Income" + " " + "Quarterly" + ".csv")
        readStr = parse_statements(readStr)
        common_lib.write_file(readStr, stockFileDir + ticker + " " + "Income" + " " + "Quarterly" + ".csv")

    #        ttmList = get_col_ttm(stockFileDir + ticker + " " + "Income" + " " + "Quarterly" + ".csv")
    #        print(ttmList)
    return

# The meat of this programy

def do_stuff(tmpList):
#    print('in do_stuff()')

    ticker = common_lib.get_ticker_from_list(tmpList)
    ticker = common_lib.error_check_the_ticker(ticker, errorList)
    print(ticker)
    # Checks if ticker has problems. If it does, the for loop will continue in the next iteration.
    if 'error' in ticker:
        return
    else:
        #print(tmpList)
        get_statements_to_csv(common_lib.FINANCIAL_FILE_DIR, ticker)
    return

# Saves errorList into a file
def save_errorList():
    dataStr = common_lib.convert_errorList_into_dataStr(errorList)
    common_lib.write_file(dataStr, common_lib.ERROR_FILE_DIR + "download_fundamental_data_errorList.txt")
    return

def start_doing_stuff():

    # Get ticker filename
    import sys
    choiceExchangeClass.choiceExchange = common_lib.check_if_there_exist_any_system_argument(sys.argv)
    #choiceExchangeClass.choiceExchange = common_lib.TICKER_FILENAME_DEFAULT


    # Check if there exist a second system argument
    if len(sys.argv) < 2:
        flagLastPriceClass.flagLastPrice = flagLastPriceClass.flagLastPrice # This is redundant, but stated to make
                                                                            # this code more readable.
        #flagLastPriceClass.flagLastPrice = False
    else:
        flagLastPriceClass.flagLastPrice = sys.argv[2]  # Get which choice user makes in regards to last price
        flagLastPriceClass.flagLastPrice = bool(flagLastPriceClass.flagLastPrice)

    tmpList = common_lib.get_col_symbol(common_lib.TICKER_FILE_DIR + choiceExchangeClass.choiceExchange)
#    tmpList = ['TRC/WS','LOV','PCG^I','IDN','INO','INFU','IG','IBO','IBIO','HUSA','HEB','GRH','GTE','HRT','AMCO','AMS','ALN','APT','ANV','AXX','AIRI','ACY','ADK','ACU','ETF','IAF']
    tmpList = ['CELP']

    tmpInt = len(tmpList)
    for x in range(0, tmpInt):
        print("in download_fundamental_data.py")
        def newfunc():
            #print('in newfunc()')
            do_stuff(tmpList)
            return
        numSec = timeit.timeit(newfunc, number=1)
        common_lib.estimated_time_left(x, tmpInt, numSec)


#    print_list(finalList)
    save_errorList()
    return

# Prints the run time of this program
def actual_run_time():

    def new_function():
        start_doing_stuff()
        return
    numSec = timeit.timeit(new_function, number=1)
    from datetime import timedelta
    floatOfNumSec = timedelta(seconds=float(numSec))
    print('Actual run time: ' + str(floatOfNumSec))
    return

def main():
    actual_run_time()
    return

main()
