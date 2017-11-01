import os
import csv
import time
from config import stock, year

os.chdir('../')
c_year = year
c_stock = stock
latest_year = int(time.strftime("%Y"))
total_data = []

while c_year <= latest_year:
    for count_month in range(1, 13):
        str_year = str(c_year)
        if count_month < 10:
            str_month = '0' + str(count_month)
        else:
            str_month = str(count_month)

        file_name = 'stock-' + c_stock + '-' + str_year + '-' + str_month + '.csv'


        file = open('data/' + file_name, 'r', encoding='big5')
        csv_cursor = csv.reader(file)
        temp_list = []
        for row in csv_cursor:
            temp_list.append(row)

        try:
            row_num = 2
            while len(temp_list[row_num]) > 2:
                total_data.append(temp_list[row_num])
                row_num += 1
        # print(row_num)
        except:
            pass

        file.close()

        count_month += 1
    c_year += 1


result_file = open('total-data-' + stock + '-.csv', 'w')
csv_cursor = csv.writer(result_file)

for row in total_data:
    csv_cursor.writerow(row)


print('Sucessfully')
