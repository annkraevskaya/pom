from pages.login_page import LoginPage
from pages.account_pages.products_page import ProductsPage



class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)




