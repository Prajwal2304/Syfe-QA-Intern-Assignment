from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Remove Item from Cart
def remove_item_from_cart(driver):
    try:
        driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(2)

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        removed = False

        for item in cart_items:
            price_element = item.find_element(By.CLASS_NAME, "inventory_item_price")
            price_text = price_element.text.replace("$", "")
            price = float(price_text)

            if 8 <= price <= 10:
                remove_button = item.find_element(By.XPATH, ".//button[text()='Remove']")
                remove_button.click()
                print(f"Removed item with price ${price}.")
                removed = True
                break

        if not removed:
            raise Exception("No item found with a price between $8 and $10.")

        # check cart count
        try:
            cart_icon = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            cart_count = int(cart_icon.text)
        except TimeoutException:
            cart_count = 0

        # Validate
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
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        backpack_add_button.click()
        bike_light_add_button.click()
        onesie_add_button.click()
        time.sleep(2)

        remove_item_from_cart(driver)

    finally:
        driver.quit()