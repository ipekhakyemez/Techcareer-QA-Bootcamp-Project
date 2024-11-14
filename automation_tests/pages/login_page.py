from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "login-email")  
        self.password_field = (By.ID, "login-password-input")  
        self.login_button = (By.CSS_SELECTOR, "button.q-primary")  
        self.error_message = (By.CSS_SELECTOR, "span.message")  
        self.cookie_button = (By.ID, "onetrust-accept-btn-handler")  
        self.hesabim_element = (By.CSS_SELECTOR, "div.link.account-user")  

    def close_cookies(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.cookie_button)).click()

    def enter_username(self, username):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.login_button)).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.error_message)).text

    def is_logged_in(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.hesabim_element)).is_displayed()
