from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
import allure



@allure.feature('Order products')
def test_making_an_order(page: Page):
    login_page = LoginPage(page)
    add_products = MainPage(page)


    #Успешная авторизация
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Input login and password"):
        login_page.input_login()
        login_page.input_password()
        login_page.click_button_enter()
    time.sleep(2)

    #Добавление нескольких товаров в корзину
    with allure.step("Add four products in basket"):
        add_products.add_four_product_in_basket()
    time.sleep(2)

    #Переход в корзину
    with allure.step("Go in basket"):
        add_products.go_to_basket()
    time.sleep(2)

    #Успешное оформление товара
    with allure.step("Successful order"):
        add_products.making_an_oreder()
    time.sleep(2)
