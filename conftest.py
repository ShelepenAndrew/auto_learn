import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # чтобы тесты выполнялись в фоне (без открытия в браузере). GIT

@pytest.fixture()
def driver():
    options = Options() # чтобы тесты выполнялись в фоне (без открытия в браузере). GIT
    options.add_argument('--headless') # чтобы тесты выполнялись в фоне (без открытия в браузере). GIT
    driver = webdriver.Chrome(options=options) #в скобках options=options чтобы тесты выполнялись в фоне (без открытия в браузере). GIT
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()