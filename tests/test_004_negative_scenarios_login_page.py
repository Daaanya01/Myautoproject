
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage
import allure

@allure.feature("Entering empty values")
def  test_input_with_empty_fields(page: Page):
    login_page = LoginPage(page)

    #Открытие страницы логина
    with allure.step("Open login page"):
        login_page.open()
    #Нажатие на кнокпу ЛОГИН
    with allure.step("Click button login"):
        login_page.click_button_enter()
    #Проверка ошибки при попвытке залогинится с пустыми значениями
    with allure.step("check allert empty values"):
        login_page.input_with_empty_fields()

@allure.feature("Empty password")
def test_input_login_and_not_input_password(page: Page):
    login_page = LoginPage(page)
    # Открытие страницы логина
    with allure.step("Open login page"):
        login_page.open()

    #Ввод корректного логина + нажатие на кнопку ЛОГИН
    with allure.step("Input corrected login"):
        login_page.input_login()
        login_page.click_button_enter()

    #Проверка появления ошибки при попытке входа без пароля
    with allure.step("Check allert not password"):
        login_page.empty_password()


