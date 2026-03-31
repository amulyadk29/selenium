from selenium import webdriver
from utility import get_rows, get_columns, read_data
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://sbi.bank.in/web/student-platform/maturity-value-calculator")
driver.maximize_window()
sleep(2)

filename = r"C:\Users\Admin\OneDrive\Documents\Book1.xlsx"

rows = get_rows(filename,"Sheet1")

for row in range(2,rows+1):
    amount = read_data(filename,"Sheet1",row,1)
    prd1 = read_data(filename, "Sheet1", row, 2)
    prd2 = read_data(filename, "Sheet1", row, 3)
    roi = read_data(filename, "Sheet1", row, 4)
    expected_1 = read_data(filename, "Sheet1", row, 5)

    print(amount,prd1,prd2,roi,expected_1)

driver.close()