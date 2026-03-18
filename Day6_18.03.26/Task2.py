# Task 2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")
sleep(5)

driver.find_element(By.ID, "firstName").send_keys("Justin")
driver.find_element(By.ID, "lastName").send_keys("Bieber")

driver.find_element(By.ID, "userEmail").send_keys("connect@JB123.com")

driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()

driver.find_element(By.ID, "userNumber").send_keys("9119119119")

subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Social Studies")
subjects.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']").click()
driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3']").click()

choose_file = driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\DELL\Downloads\Wallpaper.jpg")

driver.find_element(By.ID, "currentAddress").send_keys("Gurgaon, NCR")

driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)

driver.find_element(By.ID, "react-select-4-input").send_keys("Gurgaon")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

driver.find_element(By.ID, "submit").click()
sleep(5)

print("Form Submitted Successfully")

driver.quit()
