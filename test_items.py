import pytest
import time
from selenium.webdriver.common.by import By

# Ссылка на страницу товара
PRODUCT_URL = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestShoppingCart():
    def test_presence_of_add_to_cart_button(self, browser):
        # Инициализация: открываем веб-страницу с товаром
        browser.get(PRODUCT_URL)
        time.sleep(30)  

        # Действие: находим кнопку для добавления товара в корзину
        cart_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')

        # Проверка: убедимся, что кнопка была успешно найдена на странице
        assert cart_button is not None, "Ошибка: кнопка 'Добавить в корзину' не обнаружена."