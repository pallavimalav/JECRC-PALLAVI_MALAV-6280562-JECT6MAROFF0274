from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(5)

action = ActionChains(driver)

draggable_ele = driver.find_element(By.ID,'draggable')
droppable_ele = driver.find_element(By.ID,'droppable')

action.drag_and_drop(draggable_ele, droppable_ele).perform()
sleep(5)

# assert droppable_ele.text == "Dropped!"

text = driver.find_element(By.XPATH, '(//div[@id ="droppable"]/child::p)[1]')
print("Action performed!")

sleep(5)
driver.quit()

