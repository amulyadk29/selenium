# from selenium import webdriver
# from time import sleep

# # launch browser
# driver = webdriver.Chrome()

# open website
# driver.get("http://demowebshop.tricentis.com")
# driver.maximize_window()
# sleep(3)

# # 1 ID locator
# driver.find_element("id","small-searchterms").send_keys("computer")

# # 2 Name locator
# driver.find_element("name","q").clear()
# driver.find_element("name","q").send_keys("laptop")

# # 3 Class Name locator
# driver.find_element("class name","search-box-button").click()
# sleep(3)

# driver.get("http://demowebshop.tricentis.com")
# sleep(3)

# # 4 Link Text locator
# driver.find_element("link text","Log in").click()
# sleep(3)

# driver.get("http://demowebshop.tricentis.com")
# sleep(3)

# 5 Partial Link Text locator
# driver.find_element("partial link text","Reg").click()
# sleep(3)

# driver.get("http://demowebshop.tricentis.com")
# sleep(3)

# 6 Tag Name locator
# links = driver.find_elements("tag name","a")

# for link in links:
#     print(link.text)

#     print(anchor.text,end=' - ')
#     print(anchor.get_attribute("href"))

# sleep(5)
# driver.quit()

# css selector locators
# driver.find_element("css selector","input#email").send_keys('amulya@gmail.com')
# driver.find_element("css selector","input.email").send_keys('BYE')
# driver.find_element("class name","button-1.login-button").click()

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://demowebshop.tricentis.com")

#using id
# driver.find_element("css selector","#small-searchterms").send_keys("laptop")

# using class
# driver.find_element("css selector",".search-box-button").click()
# sleep(5)

# using tag + id
# driver.find_element("css selector","input#small-searchterms").send_keys("phone")

# using tag + class
# driver.find_element("css selector","input.search-box-button").click()
# sleep(5)

# driver.quit()