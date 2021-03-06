parseStockData v0.1
==============

______________________________________________________
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
______________________________________________________

Created by Gary Lau

Requires Python 3.3

This program will grab financial data from the web and save them on csv file. All of this is done through command line (I'm working on implementing the GUI).

Before running this program, specify where to store the info. Find 'common_lib.py', search 'STOCK_FILE_DIR' and change the file address.

Then run index.py to start. 

It will give you an option of whether to download a list of tickers first. If this is your first time running the program, type 'Y'. Otherwise, type 'N', since it's unnecessary.

Next, it will ask which exchange to download from. Before selecting 'all', please read the CAUTION below.

Next, it will ask if you wish to download 'Last Price' only. If this is your first time running the program or you want to update the financial data from the web, type 'N' in order to get full financial data from selected exchanges. Otherwise, type 'Y' for running time purposes.


CAUTION:
Downloading all the financial data at a single time from the web will take around 24 hours, with no pause download feature. I recommend downloading from individual exchanges first.
