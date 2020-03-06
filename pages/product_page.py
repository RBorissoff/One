from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "There's no \'Add to cart\' button on the page"

    def should_be_promo_in_the_url(self):
        assert "promo=newYear" in self.browser.current_url, "There's no promo in the link"

    def add_item_to_cart(self): # два assert, т.к. оба проверяемых сообщения появляются после добавления товара
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()
        self.solve_quiz_and_get_code() # считывает x, выполняет расчет по формуле, вставляет значение, жмет ок 
        assert "The shellcoder's handbook" in self.browser.find_element(*ProductPageLocators.ADDED_BOOK).text, "Added to cart book and chosen one are different"
        assert "9,99" in self.browser.find_element(*ProductPageLocators.TOTAL_COST_IN_CART).text, "Another book amount in basket"

# 