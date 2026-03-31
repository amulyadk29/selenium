import openpyxl
from openpyxl.styles import PatternFill

file = r"C:\Users\Admin\Downloads\xL.xlsx"

def get_rows(file, sheetname):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    return sheet.max_row

def get_columns(file, sheetname):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    return sheet.max_column

def write_data(file, sheetname, row, column, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    sheet.cell(row, column).value = data
    workbook.save(file)

def read_data(file, sheetname, row, column):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    return sheet.cell(row, column).value

def fill_green(file,sheetname,row,column):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    green_color = PatternFill(fill_type='solid',start_color='00ff00')
    sheet.cell(row ,column).fill = green_color
    workbook.save(file)

def fill_red(file,sheetname,row,column):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    red_color = PatternFill(fill_type='solid',start_color='ff0000')
    sheet.cell(row ,column).fill = red_color
    workbook.save(file)
