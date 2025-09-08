import allure
from base.base_pages import BasePage

class CheckoutYourInfoPage(BasePage):

    _PAGE_URL ="https://www.saucedemo.com/checkout-step-one.html"


    # Локторы кнопок на странице Checkout-Your Information:

    _FIRST_NAME = "//input[@class='input_error form_input']"
    _LAST_NAME = "xpath", "//input[@id='last-name']"
    _ZIP_POSTAL_CODE = "//input[@id='postal-code']"
    _CANCEL_BUTTON = "//button[@name='cancel']"
    _CONTINUE_BUTTON = "//input[@type='submit']"

    # Методы взпимодействия с шагами:

    @allure.step("Ввод имени")
    def first_name_input(self):
        self.driver.find_element(*self._FIRST_NAME).send_keys("Hanna")

    @allure.step("Ввод фамилии")
    def last_name_input(self):
        self.driver.find_element(*self._LAST_NAME).send_keys("Kraevskaya")

    @allure.step("Ввод индекса")
    def zip_postal_code_input(self):
        self.driver.find_element(*self._ZIP_POSTAL_CODE).send_keys("1234567")

    @allure.step("Клик на кнопку 'Continue'")
    def click_continue_button(self):
        self.driver.find_element(*self._CONTINUE_BUTTON).click()






