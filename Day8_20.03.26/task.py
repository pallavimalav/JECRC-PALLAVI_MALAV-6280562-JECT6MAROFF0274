# Task 1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

driver.get(r'C:\Users\DELL\Desktop\Projects PyCharm\Day8_20.03.26\playlist.html')
driver.maximize_window()

songs = driver.find_element(By.ID,'songs')
select = Select(songs)

if select.is_multiple:
    justin = driver.find_elements(By.XPATH,'//select[@id="songs"]/descendant::optgroup[5]')
    for i in justin:
        select.select_by_visible_text(i.text)

print([i.text for i in select.all_selected_options])

# print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()


sleep(5)
driver.quit()





