import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def driver (request):

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)  # autouse=True - выполняется автоматически для всех тестов
def auto_login(driver):  # Получаем driver как зависимость
        """Фикстура для автоматической авторизации перед каждым тестом"""
        # Переходим на страницу логина
        driver.get("https://www.saucedemo.com/")

        # Выполняем авторизацию
        driver.find_element("xpath", "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
        driver.find_element("xpath", "//input[@type='submit']").click()