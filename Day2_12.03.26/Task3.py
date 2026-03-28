# for-loop to open the title & name of the website with the help of different browsers.

from selenium import webdriver
from time import sleep


from selenium import webdriver
import time

browsers = [
    webdriver.Chrome,
    webdriver.Edge,
    webdriver.Firefox
]

for browser in browsers:
    driver = browser()
    driver.get("https://www.lenskart.com/")
    print(f'Current_URL: {driver.current_url}')
    print(f'Title: {driver.title}')
    print(f'Author: {driver.name}')
    time.sleep(2)
    driver.quit()
