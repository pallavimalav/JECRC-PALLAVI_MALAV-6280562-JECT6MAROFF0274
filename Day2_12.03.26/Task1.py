# script-1 :- to perform all the methods in a script


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(5)

driver.maximize_window()
sleep(5)
driver.minimize_window()
sleep(5)
driver.back()
sleep(5)
driver.forward()
sleep(5)
driver.refresh()
sleep(5)


opts = webdriver.ChromeOptions()
# these will make sure that driver won't close automatically
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/")
driver.maximize_window()



driver.close()
driver.quit()




