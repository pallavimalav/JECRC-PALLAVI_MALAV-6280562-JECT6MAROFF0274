# screenshot
# in robot framework its a built in keyword

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

folder = os.path.join(os.getcwd(),'screenshot')
os.makedirs(folder,exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
action = ActionChains(driver)
driver.maximize_window()

sleep(3)

driver.save_screenshot(f'{folder}/full_page.png')
sleep(3)

ele = driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
# //img[contains(@alt,"Photo of a woman in a cherry-patterned ")]
action.scroll_to_element(ele).perform()
sleep(3)

ele.screenshot(f'{folder}/cherry_red.png')
sleep(3)

# //
# //



driver.quit()

