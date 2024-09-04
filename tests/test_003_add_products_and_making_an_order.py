from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage

def test_making_an_order(page: Page):
    login_page = LoginPage(page)
    add_products = MainPage(page)

    #Успешная авторизация
    login_page.open()
    login_page.input_login()
    login_page.input_password()
    login_page.click_button_enter()
    time.sleep(2)

    #Добавление нескольких товаров в корзину
    add_products.add_four_product_in_basket()
    time.sleep(2)

    #Переход в корзину
    add_products.go_to_basket()
    time.sleep(2)

    #Успешное оформление товара
    add_products.making_an_oreder()
    time.sleep(2)
