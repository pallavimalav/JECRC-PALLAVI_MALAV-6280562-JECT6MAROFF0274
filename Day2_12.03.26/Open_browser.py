# to open Chrome browser
from selenium import webdriver
from time import sleep


# driver = webdriver.Chrome()
# sleep(5)
# # driver =  webdriver.Edge()
# # sleep(5)
# # driver = webdriver.Firefox()
# # sleep(5)
# driver.get("https://supertails.com/")
# driver.maximize_window()
# sleep(2)
# # driver.minimize_window()
# # sleep(4)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(3)


opts = webdriver.ChromeOptions()
# these will make sure that driver won't close automatically
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://supertails.com/")
driver.maximize_window()

# try the same functions with edge & firefox.

# opts = webdriver.FirefoxOptions()
# # these will make sure that driver won't close automatically
# opts.set_preference("detach", True)
# driver = webdriver.Firefox(options=opts)
#
# driver.get("https://supertails.com/")
# driver.maximize_window()

# driver.close()

driver.quit()


# method to get the title of url










