# from openpyxl import load_workbook
import openpyxl

filename = r"C:\Users\Admin\Downloads\xL.xlsx"
workbook = openpyxl.load_workbook(filename)
sheet = workbook.active
# sheet = workbook["Sheet2"]
rows = sheet.max_row
cols = sheet.max_column

for row in range(1,rows+1):
    for col in range(1,cols+1):
        print(sheet.cell(row=row,column=col).value,end='')
        print()

sheet.cell(row=1,column=3).value= "i"
sheet.cell(row=2,column=3).value= "j"
sheet.cell(row=3,column=3).value= "k"

workbook.save(filename)
# # print(sheet.cell(row=1,column=3).value)
# # print(sheet.cell(row=2,column=3).value)
# # print(sheet.cell(row=3,column=3).value)