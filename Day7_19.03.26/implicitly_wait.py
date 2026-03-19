# implicitly waits : waits for the element until it finds the element.
# no such element found exception.

# dont use implicitly wait & explicitly wait together cause they will overlap.

# driver.implicitly_wait(5)
#
# wait = WebDriverWait(driver, 5)
#
# enable_btn = wait.until(EC.element_to_be_clickable((By.ID,'enableAfter')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep


driver = webdriver.Chrome()


driver.get("https://abc.com/")
driver.maximize_window()
# wait is in by default seconds
# only applicable for driver.find_element -- it finds the element in the DOM structure // it is a global wait.

driver.implicitly_wait(3)

# ele = driver.find_element(By.XPATH,'(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(ele.get_attribute('src'))

ele = driver.find_element(By.XPATH,' (//a[@class="AnchorLink"]/parent::li/descendant::span[3])')
print(ele.text)

driver.quit()

