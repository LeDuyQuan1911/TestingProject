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
def test_addSupplyAdmin(driver):
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)

    login_button = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login_button)
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("admin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()


    wait = WebDriverWait(driver, 10)  # Chờ tối đa 10 giây
    first_row = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placeholder')))
    first_row_info = first_row.find_element(By.CLASS_NAME, 'info')
    album_username = first_row_info.find_elements(By.CLASS_NAME, 'item')[2].text.strip()  # Tên album (index 2)
    album_quantity = first_row_info.find_elements(By.CLASS_NAME, 'item')[6].text.strip()  # Giá trị ở index 6
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[5]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="supplyRecord"]/div[1]/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="new-supply"]/div/div[3]/div[3]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="my-input"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="my-input"]').send_keys("2-"+album_username)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="add_exist_album"]/div/div[2]/input[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="new-supply"]/div/div[3]/div[2]/div/div/div[3]/input').send_keys(100)
    driver.find_element(By.XPATH, '//*[@id="new-supply"]/div/div[3]/div[2]/div/div/div[4]/input').send_keys(100)
    driver.find_element(By.XPATH, '//*[@id="new-supply"]/div/div[4]/div[2]/div[2]').click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    first_row = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placeholder')))
    first_row_info = first_row.find_element(By.CLASS_NAME, 'info')
    album_usernameCheck = first_row_info.find_elements(By.CLASS_NAME, 'item')[2].text.strip()
    album_quantityCheck = first_row_info.find_elements(By.CLASS_NAME, 'item')[6].text.strip()
    assert album_usernameCheck == album_username, "Không trùng tên album"
    assert int(album_quantityCheck) == int(album_quantity) + int(100), "Không trùng số lượng sản phẩm thêm vào"



        

    






