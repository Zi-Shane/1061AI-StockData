import os
import time
import socket

socket.setdefaulttimeout(2)
from urllib.request import urlretrieve
from config import stock, year

d_year = year
d_stock = stock
latest_year = int(time.strftime("%Y"))
count_month = 1

try:
    os.mkdir('data')
except:
    print('Already have data folder')

os.chdir('data')

while d_year <= latest_year:

    while count_month <= 12:
        str_year = str(d_year)
        if count_month < 10:
            str_month = '0' + str(count_month)
        else:
            str_month = str(count_month)

        url = ('http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=' 
                    + str_year 
                    + str_month 
                    + '01&stockNo=' + d_stock)  
        file_name = 'stock-' + d_stock + '-' + str_year + '-' + str_month + '.csv'

        time.sleep(3)
        try:
            print('Downloading ' + 'stock-' + d_stock + '-' + str_year + '-' + str_month)
            urlretrieve(url, file_name)
            count_month += 1
        except:
            print('Timeout')
            print('Try again! ', end=' ')
            continue
        
    d_year = d_year + 1
    count_month = 1

print('Downloads complete!', end="\n")
