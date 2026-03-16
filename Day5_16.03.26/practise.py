from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# radio-buttons : user-input and later either if-else or toggle

gender=input("enter your gender")

if gender == "Male":
 driver.find_element(By.ID,'male').click()
else:
 driver.find_element(By.ID,'female').click()


# checkboxes : first check all the checkboxes(use two x-paths) and print their values and then backwards uncheck all the checkboxes.
days = driver.find_elements(By.XPATH,'//div[@class ="form-check form-check-inline"]/input[@type="checkbox"]')
for day in days:
    day.click()
    sleep(1)
    print(day.get_attribute('value'))

for j in days[::-1]:
    j.click()
    sleep(1)


driver.quit()


