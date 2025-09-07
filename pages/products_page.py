from base.base_pages import BasePage
from conftest import driver


class ProductsPage(BasePage):

    _PAGE_URL = "https://www.saucedemo.com/inventory.html"

    # Products Locators:

    _ADD_TO_CART_BACKPACK = "//button[@name='add-to-cart-sauce-labs-backpack']"
    _ADD_TO_CART_BIKE_LIGHT ="// button[ @ id = 'add-to-cart-sauce-labs-bike-light']"
    _ADD_TO_CART_BOLT_TSHIRT = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    _ADD_TO_CART_FLEECE_JACKET = "//button[@name='add-to-cart-sauce-labs-fleece-jacket']"
    _ADD_TO_CART_ONESIE = "//button[@id='add-to-cart-sauce-labs-onesie']"
    _ADD_TO_CART_TSHIRT_RED = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"


    def click_add_to_cart_backpack(self):
        self.driver.find_element(*self._ADD_TO_CART_BACKPACK).click()

    def click_add_to_cart_bike_light(self):
        self.driver.find_element(*self._ADD_TO_CART_BIKE_LIGHT).click()

    def click_add_to_cart_bolt_tshirt(self):
        self.driver.find_element(*self._ADD_TO_CART_BOLT_TSHIRT).click()

    def click_add_to_cart_fleece_jacket(self):
        self.driver.find_element(*self._ADD_TO_CART_FLEECE_JACKET).click()

    def click_add_to_cart_onesie(self):
        self.driver.find_element(*self._ADD_TO_CART_ONESIE).click()

    def click_add_to_cart_tshirt_red(self):
        self.driver.find_element(*self._ADD_TO_CART_TSHIRT_RED).click()









