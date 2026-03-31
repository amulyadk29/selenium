# from selenium import webdriver
# from selenium.trial import get_columns

# file = r"C:\Users\Admin\Downloads\xL.xlsx"
#
# rows = get_rows(file,"Sheet1")
# columns = get_columns(file,"Sheet1")
#
# for row in range(2,rows+1):
#     for col in range(1,columns+1):
#        print(read_data(file,'Sheet1',row,col),end=' ')
#     print()

from utility import get_rows, get_columns, read_data

file = r"C:\Users\Admin\Downloads\xL.xlsx"

rows = get_rows(file, "Sheet1")
columns = get_columns(file, "Sheet1")

for row in range(2, rows + 1):
    for col in range(1, columns + 1):
        print(read_data(file, "Sheet1", row, col), end=' ')
    print()