# Task 2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://qavbox.github.io/demo/signup/")

wait_obj = WebDriverWait(driver, 5)

name = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//input[@id="username"]')))
name.send_keys("Justin Bieber")

email = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//input[@id="email"]')))
email.send_keys("connect@jb123")

tel = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//input[@id="tel"]')))
tel.send_keys("555555555")

# fax = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//input[@id="fax"]')))
# fax.click()

files = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//input[@multiple="multiple"]')))
files.send_keys(r"C:\Users\DELL\Downloads\Wallpaper.jpg")

gender = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//option[@value="male"]')))
gender.click()

exp = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//input[@name="experience"][3]')))
exp.click()

skills1 = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="ip"][2]')))
skills2 = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//input[@id="ip"][5]')))
skills3 = wait_obj.until(EC.presence_of_element_located((By.XPATH, '//input[@id="ip"][6]')))
skills1.click()
skills2.click()
skills3.click()

tools = wait_obj.until(EC.presence_of_element_located((By.XPATH,'//option[@value="selenium"]')))
tools.click()


submit = wait_obj.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='submit']")))
submit.click()

print("Form successfully submitted!")

driver.quit()
sleep(5)
