from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(3)

eye=driver.find_element(By.ID,'lrd1')
# to get the inner text
# print(eye.text)

# assert is a python keywors
# to make sure the application closes only when the assert works
assert 'EYEGLASSES' in eye.text, 'didnt find'

# to get the assertion error
# assert 'GLASSES' == eye.text, 'didnt find'

print('success')


driver.quit()
sleep(3)
