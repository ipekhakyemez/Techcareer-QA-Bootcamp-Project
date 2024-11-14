from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from tests.test_login import TestLogin

class CartPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.cookie_button = (By.ID, "onetrust-accept-btn-handler") 
        self.add_to_basket_button_locator = 'div.add-to-basket-button-text'
        self.size_selector_locator = 'div.sp-itm'
        self.product_detail_container_locator = 'div.product-detail-container'
        self.product_link_locator = 'div.p-card-chldrn-cntnr a'

        
    def close_cookies(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.cookie_button)).click()


    def search_for_product(self, product_name):
        search_input = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="suggestion"]')))
        search_input.send_keys(product_name)

        search_button = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'i[data-testid="search-icon"]')))
        search_button.click()


    def open_product_page(self):

        product_link = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, self.product_link_locator)))

        current_window = self.driver.current_window_handle

        product_link.click()

        WebDriverWait(self.driver, 5).until(
            lambda driver: len(driver.window_handles) > 1)  

        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)

        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, self.product_detail_container_locator)))



    def add_to_basket_with_size_check(self):

        ok_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button.onboarding-popover__default-renderer-primary-button")))
        ok_button.click()
        try:

            size_elements = WebDriverWait(self.driver, 5).until(
                ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.sp-itm')))
            
            if size_elements:
                print("Beden seçimi yapılacak.")

                size_elements[0].click()  

                add_to_basket_button = WebDriverWait(self.driver, 5).until(
                    ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.add-to-basket-button-text')))
                add_to_basket_button.click()
            else:
                print("Beden seçimi yok, doğrudan sepete ekleniyor.")

                add_to_basket_button = WebDriverWait(self.driver, 5).until(
                    ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.add-to-basket-button-text')))
                add_to_basket_button.click()

            WebDriverWait(self.driver, 2) 

        except TimeoutException:
            print("Timeout: Beden seçimi bulunamadı, doğrudan sepete ekleniyor.")

            add_to_basket_button = WebDriverWait(self.driver, 5).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.add-to-basket-button-text')))
            add_to_basket_button.click()

            WebDriverWait(self.driver, 2) 

    def go_to_cart(self):

        basket_link = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "a.link.account-basket")))
        basket_link.click()


    def check_basket_item_quantity(self):

        basket_item_quantity_input = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, ".pb-basket-item-counter-wrapper .counter-content")))

        basket_item_quantity = basket_item_quantity_input.get_attribute("value")
        return basket_item_quantity
    

    def increase_product_quantity(self):

        basket_item_quantity_input = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, ".pb-basket-item-counter-wrapper .counter-content")))

        initial_quantity = int(basket_item_quantity_input.get_attribute("value"))

        increase_button = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.ty-numeric-counter-button[aria-label="Ürün adedi arttırma"]')))
        increase_button.click()

        WebDriverWait(self.driver, 5)  

        updated_quantity = int(basket_item_quantity_input.get_attribute("value"))
        return initial_quantity, updated_quantity


    def remove_product_from_basket(self):

        remove_button = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-saving-remove-button"))
        )
        remove_button.click()

        WebDriverWait(self.driver, 2)  

        removed_item_message = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, ".pb-basket-item-removed-item-information-label")))

        return removed_item_message.text
