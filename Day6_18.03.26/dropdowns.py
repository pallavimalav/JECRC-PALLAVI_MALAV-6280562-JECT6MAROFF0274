from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window() # so the elements dont overlap
sleep(3)
# dropdowns will be in select tag
country_dropdown = driver.find_element(By.ID,'country')
dropdown = Select(country_dropdown)

# for dropdowns : by index, by visible text, by value
dropdown.select_by_value('australia')
sleep(3)
dropdown.select_by_index(4)
sleep(3)
dropdown.select_by_visible_text('Japan')
sleep(3)
# if doesnt work because of the spaces, then add the spaces.

driver.quit()
