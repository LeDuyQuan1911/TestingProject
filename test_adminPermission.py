import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Test case for admin login and role management
def test_role_management(driver):
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

    # Navigate to role management
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[7]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="roleManager"]/div[1]/div/div').click()
    time.sleep(2)

    # Kiểm tra xem role đã tồn tại chưa
    role_name_to_check = "Chuc Nang Duy Quan Dep Trai"
    roles = driver.find_elements(By.CSS_SELECTOR, '.role-information')  # Lấy tất cả các role
    time.sleep(2)

    role_exists = False
    for role in roles:
        role_name = role.find_elements(By.CSS_SELECTOR, '.item')[2].text  # Lấy tên role (phần tử thứ 3)
        if role_name == role_name_to_check:
            role_exists = True
            break

    # Nếu role chưa tồn tại, tạo mới
    if not role_exists:
        driver.find_element(By.XPATH, '//*[@id="modal-box"]/div[1]/div[3]/input').send_keys(role_name_to_check)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="modal-box"]/div[1]/div[4]/textarea').send_keys("Duy Quan Dep Trai so mot vu tru")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="modal-box"]/div[1]/div[5]/div[1]').click()
        time.sleep(2)
        print(f"Role '{role_name_to_check}' has been created.")
    else:
        print(f"Role '{role_name_to_check}' already exists.")

    # Có thể thêm kiểm tra để xác nhận rằng role đã được tạo thành công nếu cần
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[4]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="accountManager"]/div[3]/div[1]/div/div[7]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="detail-account"]/div/div[3]/div[2]/div[1]').click()
    time.sleep(2)

    # Tìm phần tử dropdown
    dropdown = driver.find_element(By.CSS_SELECTOR, '.roleAccount')

    # Lấy tất cả các tùy chọn trong dropdown
    options = dropdown.find_elements(By.TAG_NAME, 'option')

    # Kiểm tra xem tùy chọn "Chuc Nang Duy Quan Dep Trai" có tồn tại không
    role_name_to_check = "Chuc Nang Duy Quan Dep Trai"
    role_exists = any(option.text == role_name_to_check for option in options)

    # Assert kết quả
    assert role_exists, f"Role '{role_name_to_check}' does not exist in the dropdown."

    # Nếu cần, in ra thông báo xác nhận
    print(f"Role '{role_name_to_check}' exists in the dropdown.")
    