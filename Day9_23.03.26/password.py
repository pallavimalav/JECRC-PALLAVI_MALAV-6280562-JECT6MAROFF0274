from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\DELL\Desktop\Projects PyCharm\Day9_23.03.26\index1.html')
driver.maximize_window()

action = ActionChains(driver)

driver.find_element(By.ID,'password').send_keys('neko')
sleep(2)
show_pwd = driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(2)
action.release()

sleep(2)
driver.quit()
