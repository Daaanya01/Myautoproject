from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
import allure

def test_app_state_optins(page: Page):
    login_page = LoginPage(page)
    main_page = MainPage(page)

    login_page.open()
    login_page.input_login()
    login_page.input_password()
    login_page.click_button_enter()
    main_page.add_four_product_in_basket()
    main_page.using_options_reset_app_state()
    main_page.expected_basket()