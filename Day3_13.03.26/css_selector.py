from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach" , True)
# opts.add_argument('--headless')
# Headless mode in Selenium allows you to run browser automation without opening a visible browser window, making tests faster, lighter on resources, and ideal for CI/CD pipelines. It’s widely used with Chrome and Firefox, especially when you don’t need to interact with the UI directly.
driver = webdriver.Chrome(options= opts)
driver.get("https://testautomationpractice.blogspot.com/")
# sleep(3)
driver.maximize_window()
# driver.close() # only present window will be close
# driver.quit()

sleep(1)

# basic css selector

# input[class="form-control"]
# input[type='radio']

animals = driver.find_element(By.CSS_SELECTOR,'select[id="animals"]')

# animals = driver.find_element(By.CSS_SELECTOR,'#animals')

print('worked files')

# anchor tag to find links

# <a href="https://testautomationpractice.blogspot.com/">Home</a>

# *, ^, $ : will find the first occurence.


# a[href*="testautomationpractice"]

# a[href^="http://"]


# ^ tells that my element starts w this particular string

# a[href$=".com"]

# $ : ends with


# * :- way to give partial/sub-string
# * tells this particular text is present in the original string

# drawback of css selectors: can only traverse downwards & can't find inner tags.
# in css selector can combine multiple attributes if present in the same tag.

# X - path



#

# div[class="widget-content"]
# div[class="widget-content"] a[href*="testautomationpractice.blogspot"]

driver.quit()


