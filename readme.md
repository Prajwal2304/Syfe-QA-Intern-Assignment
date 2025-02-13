# README: SauceDemo Automation Scripts

This repository contains Python scripts to automate various tasks on the [SauceDemo website](https://www.saucedemo.com/). These scripts are built using **Selenium WebDriver** and are designed to validate key functionalities such as login, adding/removing items from the cart, checkout workflow, and logout.

---

## Table of Contents
1. [Steps to Execute the Scripts](#1-steps-to-execute-the-scripts)
2. [Assumptions and Observations](#2-assumptions-and-observations)
3. [Script-wise Details](#3-script-wise-details)

---

## 1. Steps to Execute the Scripts

### Prerequisites:
- Install Python (version 3.7 or higher).
- Install Selenium:
  bash
  pip install selenium
  pip install webdriver-manager
  
- Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and ensure it's in your system's PATH.
- Clone this repository or download the scripts.

### Execution Steps:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the scripts:
   bash
   cd path/to/your/scripts
   
3. Run each script using the following command:
   bash
   python <script_name>.py
   
   Replace `<script_name>` with the name of the script you want to execute (e.g., `Task 1.py`).

4. Observe the output in the terminal. The script will print success messages or error details if any step fails.

---

## 2. Assumptions and Observations

### General Assumptions:
- The user is logged in as `standard_user` with the password `secret_sauce` for all tasks except Task 1 (Login Validation).
- The SauceDemo website behaves consistently during execution (no unexpected changes in UI or functionality).
- The WebDriver version matches the browser version installed on your system.

### Observations During Execution:
1. **Dynamic Content Loading**:
   - Some elements (e.g., buttons, dropdowns) take time to load dynamically. To handle this, explicit waits (`WebDriverWait`) are used to ensure elements are clickable or visible before interacting with them.

2. **Error Handling**:
   - Each script includes error handling for common exceptions like `NoSuchElementException`, `AssertionError`, and `TimeoutException`. If an issue occurs, the script prints detailed error messages for debugging.

3. **Case Sensitivity**:
   - Success messages (e.g., "THANK YOU FOR YOUR ORDER") are normalized to uppercase for case-insensitive comparisons to avoid mismatches due to capitalization.

4. **Cart Count Updates**:
   - The cart icon (`shopping_cart_badge`) reflects the correct item count after adding or removing items. However, if the cart is empty, the cart icon disappears, which is handled in the scripts.

5. **Logout Redirection**:
   - After logging out, the user is redirected to the login page (`https://www.saucedemo.com/`). This redirection is verified in Task 6.

---

## 3. Script-wise Details

### Task 1: Login Validation
- **Purpose**: Validate login functionality with both valid and invalid credentials.
- **Steps**:
  1. Enter valid credentials (`standard_user`, `secret_sauce`) and verify successful login.
  2. Enter invalid credentials (`invalid_user`, `wrong_password`) and verify the error message.
- **Observations**:
  - Invalid credentials display the error message: "Epic sadface: Username and password do not match any user in this service."
  - Successful login redirects to `/inventory.html`.

---

### Task 2: Add Items to Cart from Inventory Page
- **Purpose**: Add two items to the cart and verify the cart count.
- **Steps**:
  1. Change the filter to "Price (low to high)."
  2. Add "Sauce Labs Backpack" and "Sauce Labs Bike Light" to the cart.
  3. Verify that the cart icon shows `2`.
- **Observations**:
  - Sorting works as expected, and items are added to the cart successfully.
  - The cart count updates dynamically after adding items.

---

### Task 3: Add Items to Cart from Inventory Item Page
- **Purpose**: Add an item to the cart from its product details page and verify the cart count.
- **Steps**:
  1. Navigate to the product details page for "Sauce Labs Onesie."
  2. Add the item to the cart from the product details page.
  3. Verify that the cart icon shows `3`.
- **Observations**:
  - The product details page loads correctly, and the "Add to cart" button is functional.
  - The cart count increments accurately after adding the item.

---

### Task 4: Remove Items from Cart
- **Purpose**: Remove an item costing between $8 and $10 from the cart and verify the cart count.
- **Steps**:
  1. Navigate to the cart page.
  2. Identify and remove the item with a price between $8 and $10.
  3. Verify that the cart icon shows `2`.
- **Observations**:
  - The script identifies the correct item based on its price range.
  - The cart count updates correctly after removal.

---

### Task 5: Checkout Workflow
- **Purpose**: Automate the entire checkout process and verify the success message.
- **Steps**:
  1. Click "Checkout" and fill out the form with dummy data.
  2. Verify the items and total amount on the checkout overview page.
  3. Complete the purchase by clicking "Finish."
  4. Verify the success message: "THANK YOU FOR YOUR ORDER."
- **Observations**:
  - The total amount includes item prices and taxes.
  - The success message appears in uppercase, so the script normalizes it for comparison.

---

### Task 6: Logout Functionality
- **Purpose**: Automate the logout process and verify redirection to the login page.
- **Steps**:
  1. Click the burger menu icon and select "Logout."
  2. Verify redirection to the login page (`https://www.saucedemo.com/`).
- **Observations**:
  - The burger menu expands correctly, and the "Logout" option is functional.
  - Redirection to the login page is consistent and verified using the URL.

---
