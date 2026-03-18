# Task 1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
sleep(3)

checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
print("Checkboxes link found")

drag_drop_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print("Drag and Drop link found")

list_items = driver.find_elements(By.TAG_NAME, "li")
print("Total <li> elements:", len(list_items))

driver.get("https://the-internet.herokuapp.com/tables")
sleep(2)

website = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
print("Website (jdoe):", website.text)

delete_link = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='Bach']/following-sibling::td//a[text()='delete']")
print("Delete link for Bach found")

second_table = driver.find_element(By.XPATH, "(//table)[2]")
print("Second table located")

cell_100 = driver.find_element(By.XPATH, "//table[@id='table2']//td[text()='$100.00']")
parent_row = cell_100.find_element(By.XPATH, "./parent::tr")

print("Cell value:", cell_100.text)
print("Parent row text:", parent_row.text)

driver.quit()
sleep(3)