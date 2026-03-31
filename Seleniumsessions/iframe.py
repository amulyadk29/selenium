from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(2)

# ----------- 1. SINGLE IFRAME -----------
driver.find_element("xpath", "//a[normalize-space()='Single Iframe']").click()
sleep(2)

iframe1 = driver.find_element("id", "singleframe")
driver.switch_to.frame(iframe1)         #driver.switch_to.frame(name/id)
#webele(iframe) #2)index position
 
driver.find_element("xpath", "//input[@type='text']").send_keys("XYZ")
sleep(2)

driver.switch_to.default_content()   # come back to main page

# # ----------- 2. NESTED IFRAME -----------task
# driver.switch_to.parent_frame()
# driver.switch_to.default_content()

# driver.find_element("xpath", "//a[normalize-space()='Iframe with in an Iframe']").click()
# sleep(2)
#
# # outer iframe
# outer_frame = driver.find_element("xpath", "//iframe[@src='MultipleFrames.html']")
# driver.switch_to.frame(outer_frame)
#
# # inner iframe
# inner_frame = driver.find_element("xpath", "//iframe[@src='SingleFrame.html']")
# driver.switch_to.frame(inner_frame)
#
# # send keys inside inner iframe
# driver.find_element("xpath", "//input[@type='text']").send_keys("ABC")
# sleep(2)
#
# driver.switch_to.default_content()
# sleep(2)
#
# driver.quit()