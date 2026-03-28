# handling windows

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(3)

# will return particular window address & will store in this parent
parent_window = driver.current_window_handle
print(parent_window)

driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(3)

# will handle the list of all the windows present
all_windows = driver.window_handles
print(len(all_windows))

driver.switch_to.window(all_windows[-1])
print(driver.current_window_handle)

# print(driver.find_element(By.CLASS_NAME,'example').text)

# good practise to use assert
assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
driver.close()
# print('done')

driver.switch_to.window(parent_window)

driver.quit()
sleep(3)
