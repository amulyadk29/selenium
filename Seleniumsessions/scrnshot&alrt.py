# # Screenshot()---->> Syntax:
# # driver.save_screenshot("name.png")
# # driver.save_screenshot("system path/file name")
#
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# driver.get("https://staging.blinkqc.ai/auth/login")
# driver.maximize_window()
#
# sleep(5)
#
# driver.save_screenshot("First_1.png")
#
# for i in range(1, 11):
#     driver.save_screenshot(f"online{i}.png")
#     sleep(1)
#
# driver.save_screenshot(r"D:\Screenshot\First_1.png")
#
# sleep(5)
#
# driver.close()
# driver.quit()

# 2) alert mesg
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# 🔹 1. Simple Alert
driver.find_element("xpath","//button[normalize-space()='Click for JS Alert']").click()
sleep(2)

alert = driver.switch_to.alert
print(alert.text)   # print alert message
alert.accept()      # click OK

sleep(2)
print(driver.find_element("id","result").text)

#  2. Confirm Alert
driver.find_element("xpath","//button[normalize-space()='Click for JS Confirm']").click()
sleep(2)

alert = driver.switch_to.alert
print(alert.text)

alert.dismiss()   # Cancel (use accept() for OK)

sleep(2)
print(driver.find_element("id","result").text)

# 3. Prompt Alert
driver.find_element("xpath","//button[normalize-space()='Click for JS Prompt']").click()
sleep(2)

alert = driver.switch_to.alert
print(alert.text)

alert.send_keys("Hello")   # enter text
alert.accept()

sleep(2)
print(driver.find_element("id","result").text)

driver.quit()