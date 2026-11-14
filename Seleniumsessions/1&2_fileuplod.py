from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# obj4 = double_click("xpath","//button[text()='Copy Text']").click()

# Single file upload
element = driver.find_element("xpath","//h2[text()='SVG Elements']")
driver.execute_script("arguments[0].click()", element)
sleep(5)

driver.find_element("id","singleFileInput").send_keys(r"C:\Users\sipl6544\Downloads\f1-movie-4k-wallpaper-Uhdpaper.com-588050g.jpg")
sleep(5)

driver.find_element("xpath","//button[@type='submit']").click()
sleep(10)

print(driver.find_element("id","singleFileStatus"))
sleep(5)

# Double file upload
# driver.find_element("id","multipleFilesInput").send_keys(r"C:\Users\sipl6544\Downloads\Test003.17.01_17032026.xlsx")
# driver.find_element("id","multipleFilesInput").send_keys(r"C:\Users\sipl6544\Downloads\Timesheet_2026-03-01_to_2026-03-31.xlsx")
# sleep(5)
# driver.find_element("xpath","//button[normalize-space()='Upload Multiple Files']").click()
# sleep(10)
# print(driver.find_element("id","multipleFilesStatus"))