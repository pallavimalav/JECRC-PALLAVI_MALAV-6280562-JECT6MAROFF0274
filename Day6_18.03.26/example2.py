from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/")
driver.maximize_window() # so the elements dont overlap
sleep(3)

search = driver.find_element(By.XPATH,'//input[@placeholder="What are you looking for?"]')
search.clear()
print(search.text)
search.send_keys("Brown Eyeglasses" ,Keys.ENTER)
sleep(3)

SortBy_dropdown = driver.find_element(By.ID,'sortByDropdown')
dropdown = Select(SortBy_dropdown)
dropdown.select_by_value('saving')
sleep(3)

inner_text = driver.find_element(By.XPATH,'(//div[@class="sc-bf32d8a7-0 gOVKHN"])[1]/descendant::p[@class="sc-23b7d3eb-2 dQrJBg"][1]')
print(inner_text.text)

driver.quit()
