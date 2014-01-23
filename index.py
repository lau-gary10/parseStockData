'''
This is the main file to run the program.
This runs (in order):
    get_tickers.py
    download_fundamental_data.py
    get_fundamental_data_3.py

This file calls:
    common_lib.py
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
def ask_user_full_run_or_partial_run():
    print("Full run or partial run?")
    print("Type '1' for partial run. Type '2' for full run.")
    boolAnswer = input("Answer: ")
    if boolAnswer == '1':
        print("User selected partial run.")
        boolAnswer = True
    elif boolAnswer == '2':
        print("User selected full run.")
        boolAnswer = False
    else:
        print("Unknown user input. Defaulting to partial run.")
        boolAnswer = True
    return boolAnswer

def main():
    userTypeRun = ask_user_full_run_or_partial_run()
    from common_lib import check_which_exchange_user_wants_to_get_info_from, check_if_user_wants_to_download_last_price_only
    tickerFilename = check_which_exchange_user_wants_to_get_info_from()
    lastPriceFlag = check_if_user_wants_to_download_last_price_only()
    lastPriceFlag = str(lastPriceFlag)

    if userTypeRun == True:
        partial_run(tickerFilename, lastPriceFlag)
    elif userTypeRun == False:
        full_run(tickerFilename, lastPriceFlag)
    else:
        print("userTypeRun not recognized.")
    return

main()