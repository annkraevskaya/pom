import time

from pages.login_page import LoginPage
from base.base_pages import BasePage
from base.base_test import BaseTest


class TestAddToCartProducts(BaseTest):

    def test_add_to_cart_product(self):
        self.products_page.open()

        self.products_page.click_add_to_cart_backpack()
        time.sleep(1)
        self.products_page.click_add_to_cart_bike_light()
        time.sleep(1)
        self.products_page.click_add_to_cart_bolt_tshirt()
        time.sleep(1)
        self.products_page.click_add_to_cart_fleece_jacket()
        time.sleep(1)
        self.products_page.click_add_to_cart_onesie()
        time.sleep(1)
        self.products_page.click_add_to_cart_tshirt_red()
        time.sleep(1)


