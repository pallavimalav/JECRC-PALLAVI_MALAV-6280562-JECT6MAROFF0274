# opening a website in new window

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(3)

# window & tab are different instructions

# opening a website in new window

driver.switch_to.new_window('window')
sleep(5)
driver.get("https://www.cricbuzz.com/")

#


driver.switch_to.new_window('tab')
sleep(5)
driver.get("https://www.cricbuzz.com/")

sleep(3)
driver.quit()




