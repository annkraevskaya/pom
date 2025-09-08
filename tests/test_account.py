import time
import allure
import pytest     # Для маркировки тестов
from data.credentials import Credentials # Импорт класса Credentials для безопасного использования/хранения логина и пароля
from base.base_test import BaseTest  # Базовый класс тестов
from allure_commons.types import Severity  # Для указания серьезности теста



@allure.epic("Пользовательский аккаунт")
@allure.feature("Авторизация")
@allure.story("Успешная авторизация")
class TestAuthorization(BaseTest):
    @pytest.mark.smoke  # Маркировка теста как smoke
    @allure.severity(Severity.BLOCKER)  # Высокий уровень важности теста
    @allure.step("Авторизация на сайте")  # Шаг в отчете
    def test_login(self):
        self.login_page.open()  # Открываем страницу логина
        self.login_page.enter_login(Credentials.LOGIN)
        self.login_page.enter_password(Credentials.PASSWORD)
        self.login_page.login_button()
        time.sleep(2)









@allure.epic("Оформление заказа")
@allure.feature("Полный цикл покупки")
@allure.story("Добавление 3х товаров в корзину")

class TestCheckout(BaseTest):  #Создание класса тестов+наследование BaseTest

    @pytest.mark.regression  # Маркировка теста как regression
    @allure.severity(Severity.BLOCKER) # Высокий уровень важности теста
    @allure.step("Авторизация на сайте") # Шаг в отчете
    def test_login(self):
        self.login_page.open() # Открываем страницу логина
        self.login_page.enter_login(Credentials.LOGIN)
        self.login_page.enter_password(Credentials.PASSWORD)
        self.login_page.login_button()
        time.sleep(2)





    @allure.step("Добавление товара в корзину")
    def test_add_products(self):
        self.products_page.click_add_to_cart_backpack()
        # time.sleep(1)
        self.products_page.click_add_to_cart_bike_light()
        # time.sleep(1)
        self.products_page.click_add_to_cart_bolt_tshirt()
        # time.sleep(1)

    @allure.step("Переход на страницу корзины")
    def test_go_to_cart(self):
        self.products_page.go_to_cart()

        with allure.step("Проверка урла корзины"):
            assert self.driver.current_url == "https://www.saucedemo.com/cart.html" , "ошибка в урл"
        time.sleep(1)


    @allure.step("Нажатие на кнопку 'Checkout'")
    def test_click_checkout_button(self):
        self.cart_page.click_checkout_button()

        with allure.step("Проверка урла страницы 'Checkout'"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
        time.sleep(1)


    @allure.step("Заполнение информации о пользователе")
    def test_add_information_for_user(self):
        self.checkout_information.first_name_input()
        self.checkout_information.last_name_input()
        self.checkout_information.zip_postal_code_input()
        time.sleep(1)
        self.checkout_information.click_continue_button()
        with allure.step("Проверка урла страницы Checkout: Overview"):
            assert self.driver.current_url =="https://www.saucedemo.com/checkout-step-two.html"


    @allure.step("Клик на кнопку 'Finish'")
    def test_click_finish_button(self):
        self.checkout_overview.click_finish_button()
        time.sleep(1)
        with allure.step("url"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"





















