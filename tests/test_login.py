import time
import allure
from allure_commons.types import AttachmentType

from pages.login_page import LoginPage
from base.base_pages import BasePage
from base.base_test import BaseTest

@allure.epic("Пользователь")
@allure.feature("Авторизация")
class TestLogin(BaseTest):

    @allure.story("Успешный логин")
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.login_button()
        time.sleep(2)



        # self.products_page.click_add_to_cart_backpack()
        # self.products_page.click_add_to_cart_fleece_jacket()
        # time.sleep(2)


