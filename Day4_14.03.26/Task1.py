from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# 1. Navigate to Website
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(3)


# //span[text()="All"]/ancestor::div[@id="nav-main"]

# ancestor XPath:
Java = driver.find_element(By.XPATH,'//td[text()="Learn Java"]/following-sibling::td[3]')
print(Java)
print('Java course price found')

Selenium = driver.find_element(By.XPATH,'//td[text()="Amod"]/ancestor::tr/preceding-sibling::tr[4]/td[3]')
print(Selenium)
print('Selenium course found')

Same_Prices = driver.find_element(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]')
print(Same_Prices)
print('Same_Prices Found')

Names = driver.find_element(By.XPATH,'//tbody[@id="rows"]/child::tr/child::td[1]')
print(Names)
print('Names found')

driver.quit()
