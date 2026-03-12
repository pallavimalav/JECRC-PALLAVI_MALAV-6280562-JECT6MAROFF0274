# for-loop to open different web-browsers :-



from selenium import webdriver
import time

browsers = [
    webdriver.Chrome,
    webdriver.Edge,
    webdriver.Firefox
]

for browser in browsers:
    driver = browser()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(2)
    driver.quit()


