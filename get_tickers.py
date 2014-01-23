'''
This file will get a list of tickers listed in NYSE, NASDAQ, & AMEX

This link will download a list of tickers.
http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download
http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download
http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download

'''

import urllib.request
import common_lib

# Download data from the web
def get_current_ticker_from_web(urlStr, stockFileDir, downloadedFilename):
    # Get data
    response = urllib.request.urlopen(urlStr)
    html = response.read()

    # Write html to a new file
    target = open(stockFileDir + downloadedFilename, 'wb')
    target.write(html)
    target.close
    return

# Write downloaded info onto csv files
def write_stock_tickers(exchangeName):
    urlStr = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=" + exchangeName + "&render=download"
    get_current_ticker_from_web(urlStr, common_lib.TICKER_FILE_DIR, exchangeName + "Tickers.csv")
    return

# Parse the string for later use
def parse_stock_tickers_file(readStr):
    startPos = readStr.find('"Summary Quote",\n')
    endPos = len(readStr)
    readStr = readStr[startPos:endPos]
    readStr = readStr.replace('"Summary Quote",\n', '')
    return readStr

# Combine all data into one file
def combine_all_data_into_one_file(exchangeName):
    readStr = common_lib.open_file(common_lib.TICKER_FILE_DIR + exchangeName + "Tickers.csv")
    readStr = parse_stock_tickers_file(readStr)
    targetStr = open(common_lib.TICKER_FILE_DIR + "tmpFile.txt", 'a')
    targetStr.write(readStr)
    targetStr.close()
    return

# Delete unnecessary files
def pickup_garbage():
    common_lib.delete_file(common_lib.TICKER_FILE_DIR + "tmpFile.txt")
    return

def do_stuff():
    # Get rid of the older file in order to create a new file
    common_lib.delete_file(common_lib.TICKER_FILE_DIR + common_lib.OUTPUT_FILENAME)

    # Download data from the web
    for x in range(3):
        if x == 0:
            exchangeName = "nasdaq"
        elif x == 1:
            exchangeName = "nyse"
        elif x == 2:
            exchangeName = "amex"
        write_stock_tickers(exchangeName)

    # Start combining aggregate data into one file
    for x in range(0, 3):
        if x == 0:
            exchangeName = "nasdaq"
        elif x == 1:
            exchangeName = "nyse"
        elif x == 2:
            exchangeName = "amex"
        combine_all_data_into_one_file(exchangeName)
        print("function end for " + exchangeName + ".csv")

    concatenateStr = '"Symbol","Name","LastSale","MarketCap","ADR TSO","IPOyear","Sector","Industry","Summary Quote",\n'
    readStr = common_lib.open_file(common_lib.TICKER_FILE_DIR + "tmpFile.txt")

    targetStr = open(common_lib.TICKER_FILE_DIR + common_lib.OUTPUT_FILENAME, 'a')
    targetStr.write(concatenateStr)
    targetStr.write(readStr)
    targetStr.close()

    pickup_garbage()
    return

# Prints the run time of this program
def actual_run_time():
    print("In get_tickers.py")
    def new_function():
        do_stuff()
        return
    from timeit import timeit
    numSec = timeit(new_function, number=1)
    from datetime import timedelta
    floatOfNumSec = timedelta(seconds=float(numSec))
    print('Actual run time: ' + str(floatOfNumSec))
    return

def main():
    actual_run_time()
    return

main()