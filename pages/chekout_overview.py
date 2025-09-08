import allure
from base.base_pages import BasePage

class CheckoutOverviewPage(BasePage):

    _PAGE_URL ="https://www.saucedemo.com/checkout-step-two.html"


    # Локторы кнопок на странице Checkout: Overview:

    _FINISH_BUTTON= "//button[@id='finish']"
    _CANCEL_BUTTON = "//button[@id='cancel']"


    # Методы взаимодействия :

    @allure.step("Клик на кнопку 'Finish'")
    def click_finish_button(self):
        self.driver.find_element(*self._FINISH_BUTTON).click()

    @allure.step("Клик на кнопку 'Cancel'")
    def click_cancel_button(self):
        self.driver.find_element(*self._CANCEL_BUTTON).click()