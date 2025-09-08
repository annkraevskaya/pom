import allure
from base.base_pages import BasePage

class CartPage(BasePage):

    _PAGE_URL ="https://www.saucedemo.com/cart.html"

#     Локаторы кнопок в корзине:

    _CHECKOUT_BUTTON =  "//button[@class='btn btn_action btn_medium checkout_button ']"
    _CONTINUE_SHOPPING_BUTTON = "//button[@name='continue-shopping']"
    _REMOVE_BUTTON = "//button[text()='Remove']"

# Шаги:

    @allure.step("Нажать на кнопку 'Checkout'")
    def click_checkout_button(self):
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()

    @allure.step("Нажать на кнопку 'Continue Shopping'")
    def click_continue_shopping_button(self):
        self.driver.find_element(*self._CONTINUE_SHOPPING_BUTTON).click()

    @allure.step("Нажать на кнопку 'Remove'")
    def click_remove_button(self):
        self.driver.find_element(*self._REMOVE_BUTTON)




