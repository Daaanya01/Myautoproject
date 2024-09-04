from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage



def test_add_product(page: Page):
    login_page = LoginPage(page)
    add_product = MainPage(page)

#Авторизация под валидными данными
    login_page.open()
    login_page.input_login()
    login_page.input_password()
    login_page.click_button_enter()
#Добавление 1 товара в корзину
    add_product.add_one_product_in_basket()
    time.sleep(3)

def test_delete_product_from_basket(page: Page):
    login_page = LoginPage(page)
    del_product = MainPage(page)

    # Авторизация под валидными данными
    login_page.open()
    login_page.input_login()
    login_page.input_password()
    login_page.click_button_enter()
    # Добавление 1 товара в корзину
    del_product.add_one_product_in_basket()
#Переход в корзину , удаление добавленого товара, проверка, что товар удален из корзины
    del_product.go_to_basket()
    del_product.delete_product_from_basket()
