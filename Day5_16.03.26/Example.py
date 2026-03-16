from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/")
driver.maximize_window()

search = driver.find_element(By.XPATH, '//input[@placeholder="What are you looking for?"]')
search.clear()
# search.send_keys('brown eyeglasses')
# sleep(1)
search.send_keys('Brown eyeglasses', Keys.ENTER)
sleep(1)

# search.send_keys(Keys.RETURN)

# search.click()

# search = driver.find_element(By.XPATH, '//input[@placeholder="What are you looking for?"]')
# search.button.click()

print(search.get_attribute('placeholder'))
print(search.get_attribute('value'))

driver.quit()

# search = driver.find_element(By.ID, ''name'').send_keys('Brown eyeglasses', Keys.ENTER)
# search = driver.find_element(By.XPATH, '//input[@placeholder="What are you looking for?"]').click()





