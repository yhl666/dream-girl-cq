#ch4-16_ScreenLinesofConditions
import csv
import sys
import re
input_file = 'd:/ch4_demo/supplier_data.csv'
output_file = 'd:/ch4_demo/supplier_data3.csv'
pattern = re.compile(r'(001-.*)')
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)