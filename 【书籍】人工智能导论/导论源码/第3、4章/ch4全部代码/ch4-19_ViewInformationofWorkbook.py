#ch4-19_ViewInformationofWorkbook
import sys
from xlrd import open_workbook
input_file = "d:\ch4_demo\excel\sales_2013.xlsx"
workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
