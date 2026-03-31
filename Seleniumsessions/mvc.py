from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl
from time import sleep

filename = r"C:\Users\Admin\OneDrive\Documents\Book1.xlsx"
wb = openpyxl.load_workbook(filename)
sheet = wb.active

driver = webdriver.Chrome()
driver.get("https://sbi.bank.in/web/student-platform/maturity-value-calculator")
driver.maximize_window()

actions = ActionChains(driver)
sleep(2)

for row in range(2, sheet.max_row + 1):
   amount = sheet.cell(row=row, column=1).value
   period = sheet.cell(row=row, column=2).value
   period1 = sheet.cell(row=row, column=3).value
   ROI = sheet.cell(row=row, column=4).value
   # Expected = sheet.cell(row=row, column=5).value
   # Exp_Result = sheet.cell(row=row, column=6).value

   Principal=driver.find_element("id","u_amount")
   Principal.clear()
   Principal.send_keys(str(amount))
   print(amount)

   Duration = driver.find_element("id","uTime")
   Duration.clear()
   Duration.send_keys(str(period))
   print(period)

   dropdown= driver.find_element("id","selPeriodID")
   dd = Select(dropdown)
   # dd.select_by_value(str(period1))
   print(period1)

   AOI = driver.find_element("id","uRate")
   AOI.clear()
   AOI.send_keys(str(ROI))
   print(ROI)

   # ele = driver.find_element("xpath","//span[contains(@class,'ui-slider-handle ui-corner-all ui-state-default')]")
   # actions.drag_and_drop_by_offset(ele, 12,0).perform()

   sleep(2)
driver.quit()

