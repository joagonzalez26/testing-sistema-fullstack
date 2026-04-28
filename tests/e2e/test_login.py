from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_login_page_loads():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("http://localhost:5173/login")

        assert "localhost:5173" in driver.current_url
        assert "login" in driver.current_url.lower()

    finally:
        driver.quit()