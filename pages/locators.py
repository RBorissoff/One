from selenium.webdriver.common.by import By


class MainPageLocators():

	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():

	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():

	ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	ADDED_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
	TOTAL_PRICE_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
	BOOK_NAME = (By.TAG_NAME, "h1")
	BOOK_PRICE = (By.CSS_SELECTOR, "#messages > div > div.alertinner > p > strong")

# 