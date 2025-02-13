from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

#Automate Logout Function
def logout_functionality(driver):
    try:
        burger_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        burger_menu.click()
        time.sleep(2)

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()
        time.sleep(2)

        assert driver.current_url == "https://www.saucedemo.com/", "Redirection to login page failed."
        print("Test Passed: Successfully logged out and redirected to the login page.")

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

        logout_functionality(driver)

    finally:
        driver.quit()