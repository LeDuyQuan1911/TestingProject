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
# def test_checkOrderAdminOneItem(driver):
#     # Navigate to the website
#     driver.get("http://localhost/Classic-Groove-main/index.php")
#     time.sleep(2)
    
#     # Wait for and click the login button
#     login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
#     click_element(driver, login)
#     time.sleep(2)

#     # Perform login
#     driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanCustomer")
#     driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
#     driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
#     time.sleep(2)

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
#     driver.find_element(By.XPATH, '//*[@id="home"]/div[2]/div[5]').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/div[1]/div[1]').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]/div[2]').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]/div[2]').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="mycart"]/div[1]/div/div[3]/div[2]/input').click()
#     time.sleep(2)
#     totalCost = driver.find_element(By.XPATH, '//*[@id="mycart"]/div[2]/div/div[4]/div[2]').text
#     print(totalCost)
#     driver.find_element(By.XPATH, '//*[@id="mycart"]/div[2]/div/div[5]/button').click()
#     time.sleep(2)

#     # Check username
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[4]').click()
#     time.sleep(2)
#     username = driver.find_element(By.XPATH, '//*[@id="myaccount"]/div/div[1]/div[1]/div[7]/input').get_attribute('value')
#     print(username)
#     time.sleep(2)

#     # Logout
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div[1]').click()
#     time.sleep(2)
    

#     login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
#     click_element(driver, login)
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("admin")
#     driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
#     driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
#     time.sleep(2)

#     #Check order admin
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
#     time.sleep(2)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')

#     # Chuyển đổi totalCost từ chuỗi sang số (loại bỏ ký hiệu $ và chuyển đổi sang số thực)
#     totalCost_value = float(totalCost.replace('$', '').replace(',', '').strip())

#     # Kiểm tra từng đơn hàng
#     for order in order_elements:
#         # Lấy account ID (username) từ đơn hàng
#         account_id = order.find_elements(By.CLASS_NAME, 'item')[2].text.strip()  # Giả sử username là phần tử thứ 3
#         # Lấy total price từ đơn hàng
#         total_price = order.find_elements(By.CLASS_NAME, 'item')[4].text.strip()  # Giả sử total price là phần tử thứ 5
#         total_price_value = float(total_price.replace('$', '').replace(',', '').strip())  # Chuyển đổi thành float

#         # Kiểm tra điều kiện
#         if account_id == username and total_price_value == totalCost_value:
#             assert account_id == username and total_price_value == totalCost_value

#     assert account_id == username and total_price_value == totalCost_value,"Không tìm thấy sản phẩm"
        
    
def test_checkOrderAdminTwoItem(driver):
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
    driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/div[1]/div[1]').click()
    time.sleep(2)

    #Back về trang Home
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[1]').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="home"]/div[2]/div[6]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/div[1]/div[1]').click()
    time.sleep(2)

    #Page Check out
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]/div[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mycart"]/div[1]/div/div[3]/div[2]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mycart"]/div[1]/div[2]/div[3]/div[2]/input').click()
    time.sleep(2)


    totalCost = driver.find_element(By.XPATH, '//*[@id="mycart"]/div[2]/div/div[4]/div[2]').text
    print(totalCost)
    driver.find_element(By.XPATH, '//*[@id="mycart"]/div[2]/div/div[5]/button').click()
    time.sleep(2)

    # Check username
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[4]').click()
    time.sleep(2)
    username = driver.find_element(By.XPATH, '//*[@id="myaccount"]/div/div[1]/div[1]/div[7]/input').get_attribute('value')
    print(username)
    time.sleep(2)

    # Logout
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div[1]').click()
    time.sleep(2)
    

    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("admin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    #Check order admin
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')

    # Chuyển đổi totalCost từ chuỗi sang số (loại bỏ ký hiệu $ và chuyển đổi sang số thực)
    totalCost_value = float(totalCost.replace('$', '').replace(',', '').strip())

    time.sleep(2)
    # Kiểm tra từng đơn hàng
    for order in order_elements:
        # Lấy account ID (username) từ đơn hàng
        account_id = order.find_elements(By.CLASS_NAME, 'item')[2].text.strip()  # Giả sử username là phần tử thứ 3
        # Lấy total price từ đơn hàng
        total_price = order.find_elements(By.CLASS_NAME, 'item')[4].text.strip()  # Giả sử total price là phần tử thứ 5
        total_price_value = float(total_price.replace('$', '').replace(',', '').strip())  # Chuyển đổi thành float

        print(account_id)
        print(total_price)
        # Kiểm tra điều kiện
        if account_id == username and total_price_value == totalCost_value:
            assert account_id == username and total_price_value == totalCost_value

    assert account_id == username and total_price_value == totalCost_value,"Không tìm thấy sản phẩm"
        

# def test_checkOrderAdminTwoItemAndTwoQuality(driver):
#     # Navigate to the website
#     driver.get("http://localhost/Classic-Groove-main/index.php")
#     time.sleep(2)
    
#     # Wait for and click the login button
#     login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
#     click_element(driver, login)
#     time.sleep(2)

#     # Perform login
#     driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanCustomer")
#     driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
#     driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
#     time.sleep(2)

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
#     driver.find_element(By.XPATH, '//*[@id="home"]/div[2]/div[5]').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/div[1]/div[1]').click()
#     time.sleep(2)

#     #Back về trang Home
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[1]').click()
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
#     driver.find_element(By.XPATH, '//*[@id="home"]/div[2]/div[6]').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="product-details"]/div[2]/div[1]/div[1]').click()
#     time.sleep(2)

#     #Page Check out
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]/div[2]').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="mycart"]/div[1]/div[1]/div[2]/div[4]/div[4]/div/div[2]').click()
#     driver.find_element(By.XPATH, '//*[@id="mycart"]/div[1]/div/div[3]/div[2]/input').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="mycart"]/div[1]/div[2]/div[3]/div[2]/input').click()
#     time.sleep(2)


#     totalCost = driver.find_element(By.XPATH, '//*[@id="mycart"]/div[2]/div/div[4]/div[2]').text
#     print(totalCost)
#     driver.find_element(By.XPATH, '//*[@id="mycart"]/div[2]/div/div[5]/button').click()
#     time.sleep(2)

#     # Check username
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[4]').click()
#     time.sleep(2)
#     username = driver.find_element(By.XPATH, '//*[@id="myaccount"]/div/div[1]/div[1]/div[7]/input').get_attribute('value')
#     print(username)
#     time.sleep(2)

#     # Logout
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div[1]').click()
#     time.sleep(2)
    

#     login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
#     click_element(driver, login)
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("admin")
#     driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
#     driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
#     time.sleep(2)

#     #Check order admin
#     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[3]').click()
#     time.sleep(2)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     order_elements = driver.find_elements(By.CSS_SELECTOR, '.placeholder .info')

#     # Chuyển đổi totalCost từ chuỗi sang số (loại bỏ ký hiệu $ và chuyển đổi sang số thực)
#     totalCost_value = float(totalCost.replace('$', '').replace(',', '').strip())

#     time.sleep(5)
#     # Kiểm tra từng đơn hàng
#     for order in order_elements:
#         # Lấy account ID (username) từ đơn hàng
#         account_id = order.find_elements(By.CLASS_NAME, 'item')[2].text.strip()  # Giả sử username là phần tử thứ 3
#         # Lấy total price từ đơn hàng
#         total_price = order.find_elements(By.CLASS_NAME, 'item')[4].text.strip()  # Giả sử total price là phần tử thứ 5
#         total_price_value = float(total_price.replace('$', '').replace(',', '').strip())  # Chuyển đổi thành float

#         print(account_id)
#         print(total_price)
#         # Kiểm tra điều kiện
#         if account_id == username and total_price_value == totalCost_value:
#             assert account_id == username and total_price_value == totalCost_value

#     assert account_id == username and total_price_value == totalCost_value,"Không tìm thấy sản phẩm"