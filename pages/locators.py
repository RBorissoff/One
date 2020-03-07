from selenium.webdriver.common.by import By


class MainPageLocators():

	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():

	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():

	ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	ADDED_BOOK_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
	TOTAL_PRICE_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3)")
	BOOK_NAME = (By.CSS_SELECTOR, "#content_inner h1")
	BOOK_PRICE = (By.CSS_SELECTOR, "#messages > div > div.alertinner > p > strong")

# 