from selenium.webdriver.remote.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _LOGO = "//div[@class='login_logo']"


    def __init__(self, driver):
        self.driver: WebDriver = driver


    def open(self):
        self.driver.get(self._PAGE_URL)


