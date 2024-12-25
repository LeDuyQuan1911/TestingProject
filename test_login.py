import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Fixture to initialize the WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Ensure ChromeDriver is correctly installed and in PATH
    driver.maximize_window()
    yield driver
    driver.quit()

# Helper function for waiting for clickable elements
def wait_for_clickable_element(driver, locator, timeout=10):
    """Wait for an element to be clickable and return it."""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))

# Helper function for clicking an element
def click_element(driver, element):
    """Click an element safely."""
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

# Test case for admin login and validation
def test_loginAdmin(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("admin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    # Verify admin privileges
    expected_values = {
        "statistic": "statistic",
        "album": "album",
        "order": "order",
        "account": "account",
        "supply": "supply",
        "structure": "structure",
        "permission": "permission"
    }

    for field, expected_value in expected_values.items():
        element = driver.find_element(By.XPATH, f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field)+1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải admin"

    loginRoleInAdmin(driver, "admin", "superAdmin")





def test_loginCustomer(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanCustomer")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "home": "home",
        "favorites": "favorites",
        "cart": "cart",
        "account": "account",
    }

    for field, expected_value in expected_values.items():
        element = driver.find_element(By.XPATH, f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field)+1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải customer"

    loginRoleInAdmin(driver, "leduyquanCustomer", "Khách hàng")



def test_loginSeller(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanSeller")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    # Expected values for the "Seller" role
    expected_values = {
        "album": "album",
        "order": "order",
    }

    # Loop through the expected values and check if they match
    for field, expected_value in expected_values.items():
        element = driver.find_element(By.XPATH, f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field)+1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Seller"

    # Call the login role verification function
    loginRoleInAdmin(driver, "leduyquanSeller", "Seller")




def test_loginDesign(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanDesign")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "structure": "structure",
    }

    for field, expected_value in expected_values.items():
        element = driver.find_element(By.XPATH, f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field)+1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Design"

    loginRoleInAdmin(driver, "leduyquanDesign", "Desgin")


def test_loginAnalyst(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanAnalyst")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "statistic": "statistic",
        "order": "order",
        "supply": "supply"
    }

    for field, expected_value in expected_values.items():
        element = driver.find_element(By.XPATH, f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field)+1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Analyst"

    loginRoleInAdmin(driver, "leduyquanAnalyst", "Analyst")


def test_loginStocker(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanStocker")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Verify login success
    check_login = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/h3').text
    assert "Hello" in check_login, "Đăng nhập không thành công"

    expected_values = {
        "album": "album",
        "supply": "supply"
    }

    for field, expected_value in expected_values.items():
        element = driver.find_element(By.XPATH, f'//*[@id="header"]/div/div[1]/div[2]/div[{list(expected_values.keys()).index(field)+1}]/div[2]')
        actual_value = element.text.strip().lower()
        assert actual_value == expected_value, f"Lỗi: {field} không khớp, giá trị thực tế: {actual_value} - Không phải Stocker"

    loginRoleInAdmin(driver, "leduyquanStocker", "Stocker")



def test_loginEmptyUserName(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login with empty fields
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)
    
    # Check for the notice
    notice = driver.find_element(By.XPATH, '//p[@class="cart-removing" and contains(text(), "Please, enter username!")]').text
    expected_notice = "Please, enter username!"
    assert notice == expected_notice, f"Expected notice: '{expected_notice}', but got: '{notice}'"



def test_loginEmptyPasswordName(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login with empty fields
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquan")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)
    
    # Check for the notice
    notice = driver.find_element(By.XPATH, '//p[@class="cart-removing" and contains(text(), "Please, enter your password!")]').text
    expected_notice = "Please, enter your password!"
    assert notice == expected_notice, f"Expected notice: '{expected_notice}', but got: '{notice}'"


def test_loginAccountNoExist(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)
    
    # Wait for and click the login button
    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    # Perform login with non-existing account
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)
    
    # Check for the notice
    notice = driver.find_element(By.XPATH, '//p[@class="cart-removing" and contains(text(), "Account does not exist!")]').text
    expected_notice = "Account does not exist!"
    assert notice == expected_notice, f"Expected notice: '{expected_notice}', but got: '{notice}'"


def loginRoleInAdmin(driver, username, role):
    # Navigate to the website
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div').click()
    time.sleep(2)

    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("admin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)
    
    # Navigate to account section
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[4]').click()
    time.sleep(3)
    # Find all account items
    accounts = driver.find_elements(By.CLASS_NAME, 'item') 
    
    account_found = False
    
    for i in range(0, len(accounts), 7):  # Assuming each account takes 7 'item' divs
        account_username = accounts[i+1].text.strip()  # Extract username
        account_role = accounts[i+4].text.strip()  # Extract role
        
        # Check if the current account matches the input parameters
        if account_username == username and account_role == role:
            account_found = True
            break
    
    # Assert the account is found
    assert account_found, f"Account with username '{username}' and role '{role}' not found in the list."

