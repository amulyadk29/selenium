from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/")
driver.maximize_window()
sleep(3)

driver.find_element("xpath", "//*[contains(text(),'UI Testing')]").click()
sleep(3)

driver.find_element("xpath", "//*[contains(text(),'Web Elements')]").click()
sleep(3)

driver.find_element("xpath", "//*[contains(text(),'Frames')]").click()
sleep(3)

driver.find_element("xpath", "//*[contains(text(),'Iframes')]").click()
sleep(3)

# ✅ SCROLL DOWN (IMPORTANT)
iframe = driver.find_element("xpath", "//iframe")
driver.execute_script("arguments[0].scrollIntoView();", iframe)
sleep(2)

# ✅ SWITCH AFTER SCROLL
driver.switch_to.frame(iframe)

# enter data
driver.find_element("id", "username").send_keys("Admin")
driver.find_element("id", "password").send_keys("12345")

driver.find_element("xpath", "//button[contains(text(),'Login')]").click()

sleep(5)
driver.quit()