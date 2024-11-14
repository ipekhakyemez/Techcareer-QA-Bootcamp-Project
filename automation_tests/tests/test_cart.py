import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from pages.cart_page import CartPage

class TestCartPage:
    
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


    def test_add_to_cart(self):
        cart_page = CartPage(self.driver)
        cart_page.close_cookies()
        cart_page.search_for_product("çanta")
        cart_page.open_product_page()
        self.driver.execute_script("window.scrollBy(0, 250);")
        sleep(2)
        cart_page.add_to_basket_with_size_check()
        cart_page.go_to_cart()

        basket_item_quantity = cart_page.check_basket_item_quantity()
        assert basket_item_quantity == "1", f"Sepette beklenen 1 ürün var, ancak {basket_item_quantity} ürün bulundu."

    def test_increase_product_quantity(self):
        cart_page = CartPage(self.driver)
        cart_page.close_cookies()
        cart_page.search_for_product("çanta")
        cart_page.open_product_page()
        self.driver.execute_script("window.scrollBy(0, 250);")
        sleep(2)
        cart_page.add_to_basket_with_size_check()
        sleep(2)
        cart_page.go_to_cart()
        
        self.driver.execute_script("window.scrollBy(0, 250);")
        initial_quantity, updated_quantity = cart_page.increase_product_quantity()
        sleep(2)
        assert updated_quantity == initial_quantity + 1, f"Ürün adedi {initial_quantity + 1} olmalıydı, ancak {updated_quantity} bulundu."

    def test_remove_product_from_cart(self):
        cart_page = CartPage(self.driver)
        cart_page.close_cookies()
        cart_page.search_for_product("çanta")
        cart_page.open_product_page()
        self.driver.execute_script("window.scrollBy(0, 250);")
        sleep(2)
        cart_page.add_to_basket_with_size_check()
        cart_page.go_to_cart()
        
        removed_item_message = cart_page.remove_product_from_basket()
        assert "sepetinden kaldırıldı" in removed_item_message.lower(), "Ürün sepetten çıkarılmadı veya mesajı bulunamadı."
