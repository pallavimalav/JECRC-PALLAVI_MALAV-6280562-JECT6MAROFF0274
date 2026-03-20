from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=opts)

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

multi_drop  = driver.find_element(By.ID,'colors')
select = Select(multi_drop)

if select.is_multiple:
    select.select_by_value('blue')
    select.select_by_index(3)
    select.select_by_visible_text('Red')

print('before deselect:',[i.text for i in select.all_selected_options])
sleep(3)
select.deselect_by_value('blue')

print('after deselect:',[i.text for i in select.all_selected_options])

sleep(3)
driver.quit()
