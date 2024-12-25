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
def test_addFavoriteCustomer(driver):
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

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="home"]/div[2]/div[5]').click()
    time.sleep(2)

    albumName = driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/p[1]').text
    artistName = driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/p[2]').text

    driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/div[1]/div[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)


    albumNameCheck = driver.find_element(By.XPATH, '//*[@id="favorite"]/div/div/div/p[1]').text
    artistNameCheck = driver.find_element(By.XPATH, '//*[@id="favorite"]/div/div/div/p[2]').text

    assert albumName == albumNameCheck, "Tên Album không trùng nhau"
    assert artistName == artistNameCheck, "Tên Nhạc sĩ không trùng nhau"
