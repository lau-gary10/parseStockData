'''
This is the main file to run the program.
This runs (in order):
    get_tickers.py
    download_fundamental_data.py
    get_fundamental_data_3.py

This file calls:
    common_lib.py

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

# Runs get_tickers.py with error checking
def run_get_tickers_module():
    from subprocess import call
    from sys import stderr
    try:
        retcode = call("get_tickers.py", shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=stderr)
        else:
            print("Child returned", retcode, file=stderr)
    except OSError as e:
        print("Execution failed:", e, file=stderr)
    return

# Runs download_fundamental_data.py with error checking
def run_download_fundamental_data_module(tickerFilename, lastPriceFlag):
    from subprocess import call
    from sys import stderr
    try:
        retcode = call("download_fundamental_data.py" + " " + tickerFilename + " " + lastPriceFlag, shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=stderr)
        else:
            print("Child returned", retcode, file=stderr)
    except OSError as e:
        print("Execution failed:", e, file=stderr)
    return

# Runs get_fundamental_data_3.py with error checking
def run_get_fundamental_data_3_module(tickerFilename):
    from subprocess import call
    from sys import stderr
    try:
        retcode = call("get_fundamental_data_3.py" + " " + tickerFilename, shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=stderr)
        else:
            print("Child returned", retcode, file=stderr)
    except OSError as e:
        print("Execution failed:", e, file=stderr)
    return

# Runs the entire program. Long running time.
def full_run(tickerFilename, lastPriceFlag):
    run_get_tickers_module()
    run_download_fundamental_data_module(tickerFilename, lastPriceFlag)
    run_get_fundamental_data_3_module(tickerFilename)
    return

# Runs partial program. Less running time.
# It only runs download_fundamental_data.py, and get_fundamental_data_3.py
def partial_run(tickerFilename, lastPriceFlag):
    run_download_fundamental_data_module(tickerFilename, lastPriceFlag)
    run_get_fundamental_data_3_module(tickerFilename)
    return

# Asks user for full run or partial run. Returns boolean
def ask_if_user_want_to_download_list_of_tickers():
    print("Would you like to download a list of tickers first? (Y/N)")
    print("If yes, type 'Y'. If no, type 'N'.")
    print("Downloading a list of tickers will extend running time. Only select this option if you must.")
    boolAnswer = input("Answer: ")
    boolAnswer  = boolAnswer.lower()
    if boolAnswer == 'y':
        print("User selected 'Y'.")
        boolAnswer = True
    elif boolAnswer == 'n':
        print("User selected 'N'")
        boolAnswer = False
    else:
        print("Unknown user input. Defaulting to 'N'.")
        boolAnswer = True
    return boolAnswer

def main():
    userTypeRun = ask_if_user_want_to_download_list_of_tickers()
    from common_lib import check_which_exchange_user_wants_to_get_info_from, check_if_user_wants_to_download_last_price_only
    tickerFilename = check_which_exchange_user_wants_to_get_info_from()
    lastPriceFlag = check_if_user_wants_to_download_last_price_only()
    lastPriceFlag = str(lastPriceFlag)

    if userTypeRun == True:
        full_run(tickerFilename, lastPriceFlag)
    elif userTypeRun == False:
        partial_run(tickerFilename, lastPriceFlag)
    else:
        print("userTypeRun not recognized.")
    return

main()