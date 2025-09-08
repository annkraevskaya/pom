import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutYourInfoPage
from pages.chekout_overview import CheckoutOverviewPage



class BaseTest:
    @pytest.fixture(autouse=True)
    def setup_method(self, driver , request):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_information = CheckoutYourInfoPage(self.driver)
        self.checkout_overview = CheckoutOverviewPage(self.driver)







