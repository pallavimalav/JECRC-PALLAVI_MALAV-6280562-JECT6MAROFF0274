# Task 3 :

# 1. navigate to amazon
# 2. search a product through send_keys
# BUT don't click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in/")

wait_obj = WebDriverWait(driver, 10)

search = wait_obj.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
search.send_keys("bag charms")

suggestions = wait_obj.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='row']")))
suggestions[3].click()

sort_dropdown = wait_obj.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select")))
Select(sort_dropdown).select_by_visible_text("Newest Arrivals")

free_shipping = wait_obj.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Free Delivery')]")))
free_shipping.click()

products = wait_obj.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

# Looping till we find a product with price :-

for product in products:
    try:
        name = product.find_element(By.XPATH, ".//h2//span").get_attribute("textContent")
        price = product.find_element(By.XPATH, ".//span[contains(@class,'a-price-whole')]").get_attribute("textContent")

        print("Product Name:", name)
        print("Product Price:", price)
        # stopping the loop once we find the first product with our valid requirements.
        break

    except:
        continue

driver.quit()