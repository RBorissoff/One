from selenium.webdriver.common.by import By


class MainPageLocators():

	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():

	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():

	ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	ADDED_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
	TOTAL_COST_IN_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(3)")

# 