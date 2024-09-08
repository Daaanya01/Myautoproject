import allure
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage


@allure.feature('Open login page and successful login, and add one product')
def test_add_product(page: Page):
    login_page = LoginPage(page)
    add_product = MainPage(page)

#Авторизация под валидными данными
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Input login and password"):
        login_page.input_login()
        login_page.input_password()
        login_page.click_button_enter()
#Добавление 1 товара в корзину
    with allure.step("Add one product in basket"):
        add_product.add_one_product_in_basket()
    time.sleep(3)

@allure.feature('Delete product from basket')
def test_delete_product_from_basket(page: Page):
    login_page = LoginPage(page)
    del_product = MainPage(page)

    # Авторизация под валидными данными
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Input login and password"):
        login_page.input_login()
        login_page.input_password()
        login_page.click_button_enter()
    # Добавление 1 товара в корзину
    with allure.step("Add one product in basket"):
        del_product.add_one_product_in_basket()
#Переход в корзину , удаление добавленого товара, проверка, что товар удален из корзины
    with allure.step("Go in basket and delete one product from basket"):
        del_product.go_to_basket()
        del_product.delete_product_from_basket()
