from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

driver.get(r'C:\Users\DELL\Desktop\Projects PyCharm\Day8_20.03.26\playlist.html')
driver.maximize_window()

songs_list = driver.find_element(By.ID,'songs')
select = Select(songs_list)

if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text('Shape of You')
    select.select_by_visible_text('Animals')

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()
print([i.text for i in select.options])


sleep(5)
driver.quit()


