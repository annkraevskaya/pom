import allure
from base.base_pages import BasePage



class ProductsPage(BasePage):

    _PAGE_URL = "https://www.saucedemo.com/inventory.html"

    # Products Locators:

    _ADD_TO_CART_BACKPACK = "//button[@name='add-to-cart-sauce-labs-backpack']"
    _ADD_TO_CART_BIKE_LIGHT ="//button[ @ id = 'add-to-cart-sauce-labs-bike-light']"
    _ADD_TO_CART_BOLT_TSHIRT = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    _ADD_TO_CART_FLEECE_JACKET = "//button[@name='add-to-cart-sauce-labs-fleece-jacket']"
    _ADD_TO_CART_ONESIE = "//button[@id='add-to-cart-sauce-labs-onesie']"
    _ADD_TO_CART_TSHIRT_RED = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    _BASKET_ICON = "//a[@class='shopping_cart_link']"


    # ШАГИ
    @allure.step("Добавить рюкзак в корзину")
    def click_add_to_cart_backpack(self):
        self.driver.find_element(*self._ADD_TO_CART_BACKPACK).click()

    @allure.step("Добавить фонарик в корзину ")
    def click_add_to_cart_bike_light(self):
        self.driver.find_element(*self._ADD_TO_CART_BIKE_LIGHT).click()

    @allure.step("Добавить черную футболку в корзину")
    def click_add_to_cart_bolt_tshirt(self):
        self.driver.find_element(*self._ADD_TO_CART_BOLT_TSHIRT).click()

    @allure.step("Добавить флисовую куртку в корзину")
    def click_add_to_cart_fleece_jacket(self):
        self.driver.find_element(*self._ADD_TO_CART_FLEECE_JACKET).click()

    @allure.step("Добавить боди в корзину")
    def click_add_to_cart_onesie(self):
        self.driver.find_element(*self._ADD_TO_CART_ONESIE).click()

    @allure.step("Добавить красное боди в корзину")
    def click_add_to_cart_tshirt_red(self):
        self.driver.find_element(*self._ADD_TO_CART_TSHIRT_RED).click()


    def go_to_cart(self):
        self.driver.find_element(*self._BASKET_ICON).click()









