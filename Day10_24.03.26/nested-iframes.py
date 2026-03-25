from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)

# nested iframe

driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
sleep(3)

nested_iframe=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)

inner_iframe=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("123")
sleep(3)

# # methods
# driver.switch_to_parent_frame() #switches to parent frame
# driver.switch_to.default_content() # switches to default page

driver.quit()
