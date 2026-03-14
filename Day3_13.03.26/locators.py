from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach" , True)
# opts.add_argument('--headless')
# Headless mode in Selenium allows you to run browser automation without opening a visible browser window, making tests faster, lighter on resources, and ideal for CI/CD pipelines. It’s widely used with Chrome and Firefox, especially when you don’t need to interact with the UI directly.
driver = webdriver.Chrome(options= opts)
driver.get("https://testautomationpractice.blogspot.com/")
# print('its working fine')
# sleep(3)
driver.maximize_window()
# driver.close() # only present window will be close
# driver.quit()
# entire window will be quit

sleep(1)
name = driver.find_element(By.ID,'name')
phone_no = driver.find_element(By.ID,'phone')

nav_bar = driver.find_element(By.NAME,'Navbar')
radio_button = driver.find_elements(By.CLASS_NAME,'form-check-input')

# print(name)
# print('name and phone no textfield found')
# print('navigation bar found')

print(radio_button)
print(len(radio_button))


# inp = driver.find_elements(By.TAG_NAME,'input')
# print(len(inp))
driver.quit()


