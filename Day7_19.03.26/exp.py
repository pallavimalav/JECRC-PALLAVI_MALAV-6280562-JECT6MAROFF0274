from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait is a class
# import expected conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://abc.com/")
driver.maximize_window()

wait_obj = WebDriverWait(driver, 10)

loading_cicles = wait_obj.until(EC.invisibility_of_element_located((By.ID,'preloader-animated_svg__circle3')))

title_abc = driver.find_element(By.XPATH,'//span[text()="ABC SHOWS, SPECIALS & MORE"]')

assert 'SPECIALS' in title_abc.text, 'the text is not present'

print('working fine')

driver.quit()

