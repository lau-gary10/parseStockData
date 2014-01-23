parseStockData v0.1
==============

Created by Gary Lau

Requires Python 3.3

This program will grab financial data from the web and save them on csv file. All of this is done through command line (I'm working on implementing GUI).

Before running this program, specify where to store the info. Find 'common_lib.py', search 'STOCK_FILE_DIR' and change the file address.

Then run index.py to start. 

It will give you an option of whether to download a list of tickers first. If this is your first time running the program, type 'Y'. Otherwise, type 'N', since it's unnecessary.

Next, it will ask which exchange to download from. Before selecting 'all', please read the CAUTION below.

Next, it will ask if you wish to download 'Last Price' only. If this is your first time running the program or you want to update the financial data from the web, type 'N' in order to get full financial data from selected exchanges. Otherwise, type 'Y' for running time purposes.


CAUTION:
Downloading all the financial data at a single time from the web will take around 24 hours, with no pause download feature. I recommend downloading from individual exchanges first.
