from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

# copying and pasting of the address fields.

driver.get(r'C:\Users\DELL\Desktop\Projects PyCharm\Day9_23.03.26\page.html')
driver.maximize_window()

action = ActionChains(driver)

present =  driver.find_element(By.ID,'presentAddress')
permanent = driver.find_element(By.ID,'permanentAddress')

present.send_keys('JECRC, Jaipur, RJ')
sleep(2)
present.click()
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
sleep(2)
permanent.click()
sleep(2)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
sleep(2)

print("Address field copied!")

driver.quit()