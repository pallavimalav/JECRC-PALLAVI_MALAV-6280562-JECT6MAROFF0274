from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.ecosia.org/")
driver.maximize_window()
sleep(3)

search = driver.find_element(By.NAME,'q')
search.click()
print(search)

search.send_keys('amazon forest',Keys.ENTER)

print(search.get_attribute('placeholder'))
print(search.get_attribute('value'))

sleep(3)


driver.quit()
sleep(3)