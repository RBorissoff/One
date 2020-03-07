from .pages.product_page import ProductPage
import pytest


links = [
	"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019",
	"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser,link):
	page = ProductPage(browser, link) # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
	page.open()
	page.should_be_promo_in_the_url() # проверить наличие promo параметра в url
	page.should_be_add_to_cart_button() # проверить наличие кнопки "Добавить в корзину"
	page.add_item_to_cart() # проверить возможность добавления товара в корзину
	page.added_book_and_chosen_should_be_equal() # проверить совпадение имен книг
	page.prices_in_cart_and_chosen_book_should_be_equal() # проверить совпадение сумм добавленной книги и в корзине

#