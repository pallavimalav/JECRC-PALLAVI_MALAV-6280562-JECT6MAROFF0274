# multiselect dropdown

# METHODS

# select.deselect_by_index(6)
# select.deselect_all()
# print(select.first_selected_option)
# print(select.all_selected_options)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
sleep(5)

# site not working

driver.get("https://demo.mobiscroll.com/select/multiple-select")
driver.maximize_window()

multi_drop = driver.find_element(By.XPATH,'//select[@id="multiple-select-select"]')

select = Select(multi_drop)

if select.is_multiple():
    select.select_by_value('8')
    select.select_by_index(6)
    select.select_by_visible_text("Movies, Music & Games")

sleep(5)
driver.quit()






