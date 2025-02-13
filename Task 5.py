from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

#Check Workflow
def checkout_workflow(driver):
    try:
        driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(2)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        time.sleep(2)

        #fill checkout form
        first_name_field = driver.find_element(By.ID, "first-name")
        last_name_field = driver.find_element(By.ID, "last-name")
        postal_code_field = driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys("John")
        last_name_field.send_keys("Doe")
        postal_code_field.send_keys("12345")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        time.sleep(2)

        checkout_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        item_names = [item.text for item in checkout_items]

        print(f"Items in checkout: {', '.join(item_names)}")

        total_amount_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_amount = total_amount_element.text
        print(f"Total Amount: {total_amount}")

        finish_button = driver.find_element(By.ID, "finish")
        finish_button.click()
        time.sleep(2)

        #Verify Success Message
        success_message = driver.find_element(By.CLASS_NAME, "complete-header").text.strip().upper()
        expected_message = "THANK YOU FOR YOUR ORDER"

        assert success_message == expected_message, f"Unexpected success message: {success_message}"
        print(f"Test Passed: Success message displayed - '{success_message}'.")

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
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        time.sleep(2)

        #Add items to Cart
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

        checkout_workflow(driver)

    finally:
        driver.quit()