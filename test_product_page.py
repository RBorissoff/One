from .pages.product_page import ProductPage
import pytest


#В фикстуре помечаем ссылку с promo=offer7 как ожидаемо падающую (XFAIL)

@pytest.mark.parametrize("promo_offer_number",\
						["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer_number):
	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer_number}"
	page = ProductPage(browser, link) # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
	page.open()
	page.should_be_promo_in_the_url() # проверить наличие promo параметра в url
	page.should_be_add_to_cart_button() # проверить наличие кнопки "Добавить в корзину"
	page.add_item_to_cart() # проверить возможность добавления товара в корзину
	page.added_book_and_chosen_should_be_equal() # проверить совпадение имен книг
	page.prices_in_cart_and_chosen_book_should_be_equal() # проверить совпадение сумм добавленной книги и в корзине
#