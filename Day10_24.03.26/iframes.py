# iframes
# single iframe
# nested iframes

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)

# single iframe
iframe=driver.find_element(By.ID,"singleframe")
driver.switch_to.frame(iframe)
sleep(3)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("123")
sleep(3)



driver.quit()
