import allure
from base.base_pages import BasePage



class LoginPage(BasePage):

    _PAGE_URL = "https://www.saucedemo.com/"

    # Локаторы полей для авторизации:

    _LOGIN_FIELD = "//input[@placeholder='Username']"
    _PASSWORD_FIELD = "//input[@placeholder='Password']"
    _LOGIN_BUTTON = "//input[@type='submit']"

    # Шаги (методы взаимодействия)
    @allure.step("Ввод логина")
    def enter_login(self, login):
        self.driver.find_element(*self._LOGIN_FIELD).send_keys(login)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)

    @allure.step("Клик на кнопку 'LOGIN'")
    def login_button(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()