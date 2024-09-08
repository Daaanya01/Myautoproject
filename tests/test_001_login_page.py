from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage
import allure


@allure.feature('Open login page and successful login')
def test_input_login_and_password(page: Page):

    login_page = LoginPage(page)
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Input login and password"):
        login_page.input_login()
        login_page.input_password()
        login_page.click_button_enter()
    with allure.step("Check transition on main page"):
        login_page.expected_main_page()

@allure.feature('Input incorrect login and check allert')
def test_password_incor(page: Page):
    login_page = LoginPage(page)
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Input incorrect login and password"):
        login_page.input_login()
        login_page.incorrect_password()
        login_page.click_button_enter()
    with allure.step("Check allert on login page"):
        login_page.expected_allert()

@allure.feature('Open login page and successful login and logout')
def test_logout_main_page(page: Page):
    logout_page = LoginPage(page)
    with allure.step("Open login page"):
        logout_page.open()
    with allure.step("Input login and password"):
        logout_page.input_login()
        logout_page.input_password()
        logout_page.click_button_enter()
    with allure.step("successful logout for account"):
        logout_page.logout_main_page()
    time.sleep(2)
