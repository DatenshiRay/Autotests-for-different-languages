import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', 
                     action='store', 
                     default='ru', 
                     help="Выберите язык браузера")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык браузера из командной строки
    lang = request.config.getoption('language')

    # Настройка параметров для Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': lang})

    # Запускаем браузер для тестирования
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    yield driver

    # Закрываем браузер после завершения теста
    driver.quit()