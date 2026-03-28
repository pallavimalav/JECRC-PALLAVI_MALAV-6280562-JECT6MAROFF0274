# xpath axis

#example:
# <div> class = "group"
# <div> class = "group1.0"
# <div> class = "group1.1"
# <div> class = "group1.2"
# <input>id="Username"
# <label>Username

#syntax:
# relative xpath: //input[@id="Username"]
# ancestor xpath: //input[@id="Username"]/ancestor::div[@class="group1.1"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# 1. Navigate to Amazon
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)


# //span[text()="All"]/ancestor::div[@id="nav-main"]

# ancestor XPath:
Nav = driver.find_element(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"]')
print(Nav)
print('Nav bar found')

driver.quit()
# //input[@id ="twotabsearchtextbox"]/ancestor::div[@class="nav-search-field"]