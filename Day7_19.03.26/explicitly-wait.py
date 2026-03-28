# explicitly waits : waits for a particular element until the condition is satisfied.
# always confined to that particular element.
# import two conditions ; WebDriverWait & expected conditions
# throws time out error exception. doesnt specify the error condition

# from asyncio import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait is a class
# import expected conditions


driver = webdriver.Chrome()
driver.get("https://abc.com/")

wait_obj = WebDriverWait(driver, 10,poll_frequency=200)
# fluent wait : polling frequency : 500ms by default

submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID,'button')))
# submit_button = wait_obj.until(EC.url_contains("https://abc.com"))
# until is a function
submit_button.click()
# action



driver.quit()