from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "There's no \'Add to cart\' button on the page"

    def should_be_promo_in_the_url(self):
        assert "promo=newYear" in self.browser.current_url, "There's no promo in the link"

    def add_item_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()
        self.solve_quiz_and_get_code() # считывает x, выполняет расчет по формуле, вставляет значение, жмет ок

    def added_book_and_chosen_should_be_equal(self): 
        book_name = self.get_book_name()
        added_book_msg = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_MESSAGE).text
        assert book_name in added_book_msg, "Added to cart book and chosen one are different"

    def prices_in_cart_and_chosen_book_should_be_equal(self):
        book_price = self.get_book_price()
        added_book_price_msg = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_IN_CART_MESSAGE).text
        assert book_price in added_book_price_msg, "Total sum in cart is not equal to added one"

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text


# 