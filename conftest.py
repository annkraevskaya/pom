import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.credentials import Credentials
import os
from dotenv import load_dotenv


def pytest_configure():
    load_dotenv()
    if not os.getenv("STAGE"):
        os.environ["STAGE"] = "dev"


@pytest.fixture(scope="class")
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()