from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://facegenie-ams-school.web.app/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

######Vaidating Login Functionality and UI
# Check if Email Field Exists
email = driver.find_element(By.NAME, "email")
if email != None:
    print("Email Field Exists")
# Check if Password Field Exists
password = driver.find_element(By.NAME, "password")
if password != None:
    print("Password Field Exists")

driver.set_page_load_timeout(8)
email.send_keys("testbams@gmail.com")
password.send_keys("facegenie")
driver.set_page_load_timeout(8)
# Check if Log in button exists
print("Login Button Exists")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.implicitly_wait(10)
# Elements in the dashboard page are in different frames, to prove this i have printed "Main Frame" in the dashboard
driver.find_element(By.XPATH, "//p[text()='Dashboard/ Home']")
print("Main frame")
# Below UI element does not get clicked because elements are in different frames,but no iframe found in the xpath and HTML
# Automation will not be possible as the iframe is not recognised in the HTML code.
driver.find_element(By.XPATH, "(//div[@role ='button']/div/span['Log Out'])[8]").click()
