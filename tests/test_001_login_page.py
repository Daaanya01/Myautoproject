from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage


def test_input_login_and_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.input_login()
    login_page.input_password()
    login_page.click_button_enter()
    login_page.expected_main_page()


def test_password_incor(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.input_login()
    login_page.incorrect_password()
    login_page.click_button_enter()
    login_page.expected_allert()

def test_logout_main_page(page: Page):
    logout_page = LoginPage(page)
    logout_page.open()
    logout_page.input_login()
    logout_page.input_password()
    logout_page.click_button_enter()
    logout_page.logout_main_page()
    time.sleep(2)
