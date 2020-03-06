from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
	page = ProductPage(browser, link) # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
	page.open()
	page.should_be_promo_in_the_url() # проверить наличие promo параметра в url
	page.should_be_add_to_cart_button() # проверить наличие кнопки "Добавить в корзину"
	page.add_item_to_cart() # проверить возможность добавления товара в корзину

#