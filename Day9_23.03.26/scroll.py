# scroll to element
# scroll by element : positive(downwards), negative(upwards)

# SCROLL TO : (100,100)
# SCROLL BY

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://supertails.com/")
driver.maximize_window()

action = ActionChains(driver)

neko_chan = driver.find_element(By.XPATH, '//div[@data-ganame="Breed 5"]')
action.scroll_to_element(neko_chan).perform()
sleep(5)

action.scroll_by_amount(0,-1500).perform()
sleep(5)

# scroll from origin : not required rn!
# action.scroll_from_origin(neko_chan,0,500).perform()

print("Neko-chan found! <3 ")
sleep(5)

driver.quit()
sleep(5)

