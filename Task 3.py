from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Add Item to Cart
def add_item_from_details_page(driver):
    try:
        # Product Page
        driver.get("https://www.saucedemo.com/inventory.html")
        time.sleep(2)

        onesie_product_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "item_2_title_link"))
        )
        onesie_product_name.click()
        time.sleep(2) 

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart"))
        )
        add_to_cart_button.click()
        time.sleep(2) 

        # Cart Count
        cart_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        cart_count = int(cart_icon.text)

        assert cart_count == 3, f"Cart count mismatch: Expected 3, but got {cart_count}."
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
        #login
        driver.get("https://www.saucedemo.com/")
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        time.sleep(2)

        driver.get("https://www.saucedemo.com/inventory.html")
        backpack_add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        bike_light_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        backpack_add_button.click()
        bike_light_add_button.click()
        time.sleep(2)

        add_item_from_details_page(driver)

    finally:
        driver.quit()