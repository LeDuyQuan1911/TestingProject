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
def test_addAlbumAdmin(driver):
    # Navigate to the website
    driver.get("http://localhost/Classic-Groove-main/index.php")
    time.sleep(2)

    # Wait for and click the login button
    login_button = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login_button)
    time.sleep(2)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("admin")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Navigate to product manager
    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    product_manager = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="productManager"]/div[1]/div[1]/div'))
    click_element(driver, product_manager)

    # Wait for dropdown and select option
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[3]/div[2]'))
    )
    select_option = driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[3]/div[2]/select/option[3]')
    click_element(driver, select_option)

    driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[2]/div[2]/input').send_keys("Jack 97")
    driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[4]/div[2]/input').send_keys("Trịnh Trần Phương Tuấn")
    driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[6]/div[2]/input').send_keys("10000000")
    driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[8]/div[2]/textarea').send_keys("Thiên lý ơi là album kết hợp của Thiên Ân và Phương Tuấn. Đây là album tạo ra một ngôi sao trên bầu trời gọi là Jack 97")
    # Wait for the button to be clickable and click it
    add_song_button = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="new-album"]/div/div[3]/div[3]/input[2]'))
    click_element(driver, add_song_button)
    driver.find_element(By.XPATH, '//*[@id="my-input"]').send_keys("24-Thiên Lý ơi")
    driver.find_element(By.XPATH, '//*[@id="add_exist_song"]/div/div[2]/input[1]').click()
    driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[4]/div[2]/div[2]').click()

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)

    albums = driver.find_elements(By.CLASS_NAME, 'item')
    album_found = False

    for i in range(0, len(albums), 8):  
        album_name = albums[i+2].text.strip()  
        artist_name = albums[i+3].text.strip() 
        print(album_name)

        if album_name == "Jack 97" and artist_name == "Trịnh Trần Phương Tuấn":
            album_found = True
            break

    assert album_found, f"Album name 'Jack 97' by artist 'Trịnh Trần Phương Tuấn' not found in the list."

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div').click()
    time.sleep(2)

    login = wait_for_clickable_element(driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(driver, login)
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("leduyquanCustomer")
    driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Quan19112003@")
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    def check_album_and_artist():
        # Tìm tất cả các album trong grid
        albums = driver.find_elements(By.CLASS_NAME, "grid-item")  # Đảm bảo driver là đối tượng WebDriver

        # Kiểm tra tên album và nghệ sĩ
        for album in albums:
            album_name = album.find_element(By.CLASS_NAME, "title").text.strip()
            artist_name = album.find_element(By.CLASS_NAME, "artist").text.strip()
            
            if album_name == "Jack 97" and artist_name == "Trịnh Trần Phương Tuấn":
                print("Album Jack 97 và nghệ sĩ Trịnh Trần Phương Tuấn đã được tìm thấy!")
                return True
        return False

    while True:
        if check_album_and_artist():
            break
        
        try:
            load_more_button = driver.find_element(By.XPATH, '//*[@id="home"]/div[3]/div/div[3]')
            load_more_button.click() 
            time.sleep(2) 
        except Exception as e:
            print("Không thể click để tải thêm, thoát khỏi vòng lặp.")
            break







