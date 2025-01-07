import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage  


class TestLogin:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")  

        service = Service(ChromeDriverManager().install())  
        self.driver = webdriver.Chrome(service=service, options=options)

        self.driver.get("https://www.trendyol.com/giris?cb=%2F")
        self.driver.maximize_window()

        self.driver.delete_all_cookies() 

    def teardown_method(self):
        self.driver.quit()  


    def test_succesfful_login(self):
        login_page = LoginPage(self.driver)
        login_page.close_cookies()  
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login_button()

        assert login_page.is_logged_in(), "Hesabım öğesi görünmüyor, giriş başarılı olmayabilir!"

    def test_invalid_email_login(self): 
        login_page = LoginPage(self.driver)
        login_page.close_cookies()
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login_button()

        assert login_page.get_error_message() == "E-posta adresiniz ve/veya şifreniz hatalı.", \
            f"Hata mesajı beklenen değeri almadı: {login_page.get_error_message()}"

    def test_invalid_password_login(self):
        login_page = LoginPage(self.driver)
        login_page.close_cookies()
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login_button()

        assert login_page.get_error_message() == "E-posta adresiniz ve/veya şifreniz hatalı.", \
            f"Hata mesajı beklenen değeri almadı: {login_page.get_error_message()}"
