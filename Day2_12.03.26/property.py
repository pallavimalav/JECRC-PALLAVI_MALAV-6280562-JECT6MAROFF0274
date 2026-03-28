
from selenium import webdriver


opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opt)

driver.get("https://www.google.com/")
print(f'Current_URL: {driver.current_url}')
print(f'Title: {driver.title}')
print(f'Author: {driver.name}')
