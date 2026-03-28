from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

# for upload

driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()

choose_file = driver.find_element(By.ID,'file-upload')
# r makes a raw string in python
choose_file.send_keys(r"C:\Users\DELL\Downloads\Wallpaper.jpg")

submit_button = driver.find_element(By.ID,'file-submit')
submit_button.click()
sleep(5)


# for download

# driver.get("https://the-internet.herokuapp.com/download")
# driver.maximize_window()
# driver.find_element(By.XPATH,'//a[text()="Screenshot 2025-12-24 164603.png"]').click()
# sleep(3)
# print('downloaded')


driver.quit()