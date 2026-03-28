# Task 1

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.vogue.com/")
driver.maximize_window()

action = ActionChains(driver)

image = driver.find_element(By.XPATH,'(//div[@class="aspect-ratio--overlay-container"])[45]')
action.scroll_to_element(image).perform()
sleep(5)

for i in range(0,5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(3)

print("Image!")
sleep(5)

driver.quit()
sleep(5)

# action.scroll_by_amount(0,-300).perform()
# sleep(5)

