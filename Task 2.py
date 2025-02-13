from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def add_items_to_cart(driver):
    try:
        #inventory page
        driver.get("https://www.saucedemo.com/inventory.html")
        time.sleep(2)

        #Price Low to High
        filter_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        filter_dropdown.select_by_visible_text("Price (low to high)")
        time.sleep(2)

        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        bike_light_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")

        backpack_add_button.click()
        bike_light_add_button.click()
        time.sleep(2)

        #Verify Cart Count 
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        cart_count = int(cart_icon.text)

        assert cart_count == 2, f"Cart count mismatch: Expected 2, but got {cart_count}."
        print(f"Test Passed: Cart count is {cart_count}.")

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except AssertionError as e:
        print(f"Assertion failed: {e}")
    except TimeoutException as e:
        print(f"Timeout occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        time.sleep(2)

        add_items_to_cart(driver)

    finally:
        driver.quit()