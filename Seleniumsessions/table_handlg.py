from selenium import webdriver
from time import sleep

# =========================
# PART 1: WINDOW HANDLING
# =========================

driver = webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(3)

print("Window IDs:", driver.window_handles)

# Click links (open new windows)
driver.find_element("xpath", "//a[text()='Facebook']").click()
driver.find_element("xpath", "//a[text()='Google+']").click()

sleep(3)

# Switch between windows and print title
window_ids = driver.window_handles

for win in window_ids:
    driver.switch_to.window(win)
    print("Title:", driver.title)

# Switch back to main window
driver.switch_to.window(window_ids[0])

# Click Login
driver.find_element("xpath", "//a[text()='Log in']").click()
sleep(3)

# Open new tab
driver.switch_to.new_window("tab")
sleep(2)

driver.get("https://portal.blinkit.com/")
sleep(3)

# =========================
# PART 2: HANDLING TABLES
# =========================

driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

# Scroll to table
element = driver.find_element("xpath", "//h2[text()='Static Web Table']")
driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(3)

# Count rows and columns
rows = len(driver.find_elements("xpath", "//table[@name='BookTable']//tr"))
columns = len(driver.find_elements("xpath", "//table[@name='BookTable']//th"))

print("Rows:", rows)
print("Columns:", columns)

sleep(2)

# Print table data
for r in range(2, rows + 1):
    for c in range(1, columns + 1):
        data = driver.find_element(
            "xpath",
            f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]"
        ).text
        print(data, end="  ")
    print()

sleep(5)

driver.quit()