from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)


driver.get("https://supertails.com/")
driver.maximize_window()

action = ActionChains(driver)

# 100 pixels

# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
# action.send_keys(Keys.PAGE_UP).perform()
# sleep(5)

action.key_down(Keys.CONTROL).send_keys('a').perform()
sleep(5)
action.key_up(Keys.CONTROL).perform()
sleep(5)
action.key_down(Keys.CONTROL).send_keys('c').perform()
sleep(5)
action.key_up(Keys.CONTROL).perform()
sleep(5)

# pasted = action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)
# pasted.perform()
# print(pasted.text)

driver.quit()

