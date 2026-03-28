# Link-Text & Partial Link-Text:
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.LINK_TEXT,"Udemy courses")
print('i found the element using link text')


driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
print('i found the element using partial link')
# print(Partial)

driver.quit()

