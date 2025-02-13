from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

#Validate Logim
def login_validation(driver, username, password, expected_outcome):
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button.click()
        time.sleep(2)

        if expected_outcome == "Successful login":
            assert "/inventory.html" in driver.current_url, "Login failed: Not redirected to inventory page."
            print(f"Test Passed: Successful login with username '{username}'.")

        elif expected_outcome == "Invalid credentials":
            error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            expected_error = "Epic sadface: Username and password do not match any user in this service."
            assert error_message.text == expected_error, f"Unexpected error message: {error_message.text}"
            print(f"Test Passed: Invalid credentials handled correctly for username '{username}'.")

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
        #Valid Credentials
        login_validation(
            driver=driver,
            username="standard_user",
            password="secret_sauce",
            expected_outcome="Successful login"
        )

        #Invalid Credentials
        login_validation(
            driver=driver,
            username="invalid_user",
            password="wrong_password",
            expected_outcome="Invalid credentials"
        )

    finally:
        driver.quit()