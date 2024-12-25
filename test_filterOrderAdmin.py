import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select 

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
def test_filterOrderAdminPending(driver):
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

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[2]').click()
    
    # Chọn tùy chọn "Pending" từ danh sách thả xuống
    select_element = driver.find_element(By.XPATH, '//select[@onchange="loadOrderByAjax()"]')
    select = Select(select_element)  # Tạo đối tượng Select
    select.select_by_visible_text("Pending")  # Chọn tùy chọn "Pending"
    time.sleep(2)

    # Lấy tất cả các dòng trong bảng
    order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')  # Lấy tất cả các phần tử chứa thông tin đơn hàng

    # Kiểm tra trạng thái của từng dòng
    all_pending = True
    for order in order_elements:
        # Tìm phần tử trạng thái trong mỗi dòng
        status_element = order.find_elements(By.CSS_SELECTOR, '.item')[-1].text  # Lấy tất cả các phần tử con
        if status_element:
            print(f"Order Status: {status_element}")  # In ra trạng thái của đơn hàng
            if status_element != "Pending":  # Kiểm tra trạng thái
                all_pending = False
                break

    # Assert kết quả
    assert all_pending, "Not all orders are in 'Pending' status."

    print("Test completed: All orders are in 'Pending' status.")



def test_filterOrderAdminShipping(driver):
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

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[2]').click()
    
    # Chọn tùy chọn "Pending" từ danh sách thả xuống
    select_element = driver.find_element(By.XPATH, '//select[@onchange="loadOrderByAjax()"]')
    select = Select(select_element)  # Tạo đối tượng Select
    select.select_by_visible_text("Shipping")  # Chọn tùy chọn "Pending"
    time.sleep(2)

    # Lấy tất cả các dòng trong bảng
    order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')  # Lấy tất cả các phần tử chứa thông tin đơn hàng

    # Kiểm tra trạng thái của từng dòng
    all_pending = True
    for order in order_elements:
        # Tìm phần tử trạng thái trong mỗi dòng
        status_element = order.find_elements(By.CSS_SELECTOR, '.item')[-1].text  # Lấy tất cả các phần tử con
        if status_element:
            print(f"Order Status: {status_element}")  # In ra trạng thái của đơn hàng
            if status_element != "Shipping":  # Kiểm tra trạng thái
                all_pending = False
                break

    # Assert kết quả
    assert all_pending, "Not all orders are in 'Shipping' status."

    print("Test completed: All orders are in 'Shipping' status.")



def test_filterOrderAdminDelivered(driver):
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

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[2]').click()
    
    # Chọn tùy chọn "Pending" từ danh sách thả xuống
    select_element = driver.find_element(By.XPATH, '//select[@onchange="loadOrderByAjax()"]')
    select = Select(select_element)  # Tạo đối tượng Select
    select.select_by_visible_text("Delivered")  # Chọn tùy chọn "Pending"
    time.sleep(2)

    # Lấy tất cả các dòng trong bảng
    order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')  # Lấy tất cả các phần tử chứa thông tin đơn hàng

    # Kiểm tra trạng thái của từng dòng
    all_pending = True
    for order in order_elements:
        # Tìm phần tử trạng thái trong mỗi dòng
        status_element = order.find_elements(By.CSS_SELECTOR, '.item')[-1].text  # Lấy tất cả các phần tử con
        if status_element:
            print(f"Order Status: {status_element}")  # In ra trạng thái của đơn hàng
            if status_element != "Delivered":  # Kiểm tra trạng thái
                all_pending = False
                break

    # Assert kết quả
    assert all_pending, "Not all orders are in 'Delivered' status."

    print("Test completed: All orders are in 'Delivered' status.")   





def test_filterOrderAdminCancel(driver):
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

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="orderManager"]/div[1]/div/div[2]').click()
    
    # Chọn tùy chọn "Pending" từ danh sách thả xuống
    select_element = driver.find_element(By.XPATH, '//select[@onchange="loadOrderByAjax()"]')
    select = Select(select_element)  # Tạo đối tượng Select
    select.select_by_visible_text("Cancel")  # Chọn tùy chọn "Pending"
    time.sleep(2)

    # Lấy tất cả các dòng trong bảng
    order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')  # Lấy tất cả các phần tử chứa thông tin đơn hàng

    # Kiểm tra trạng thái của từng dòng
    all_pending = True
    for order in order_elements:
        # Tìm phần tử trạng thái trong mỗi dòng
        status_element = order.find_elements(By.CSS_SELECTOR, '.item')[-1].text  # Lấy tất cả các phần tử con
        if status_element:
            print(f"Order Status: {status_element}")  # In ra trạng thái của đơn hàng
            if status_element != "Cancel":  # Kiểm tra trạng thái
                all_pending = False
                break

    # Assert kết quả
    assert all_pending, "Not all orders are in 'Cancel' status."

    print("Test completed: All orders are in 'Cancel' status.")   