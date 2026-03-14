# X-path : XML Path. it is very efficient, performs better but its very slow compared to css selector & other locators.
# disadvantages of x-path: difficult to read.
# two types: relative(//) & absolute(/)


# naming convention for relative xpath:
# //input[@placeholder="Enter Name"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options= opts)
driver.get("https://testautomationpractice.blogspot.com/")
# sleep(3)
driver.maximize_window()


# driver.find_element_by_id("name").send_keys("")
# By.xpath("//input[@placeholder='Enter Name']")

Name = driver.find_element(By.XPATH,'//input[@maxlength="15"]')
# Name.send_keys("")
Email = driver.find_element(By.XPATH,'//input[@maxlength="25"]')
Phone = driver.find_element(By.XPATH,'//input[@maxlength="10"]')

print('Name, Email, Phone navigation found')

# to find inner text

# Submit = driver.find_element(By.XPATH,'//a[text()="Submit"]')
# Blog = driver.find_element(By.XPATH,'//a[text()="Blog"]')
# Youtube = driver.find_element(By.XPATH,'//a[text()="Youtube"]')
#
# print('Submit, Blog, Youtube navigation found')


driver.quit()


#  for extra-spaces : //option[contains(text(),"Blue")]




