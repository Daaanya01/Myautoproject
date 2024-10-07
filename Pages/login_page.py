from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest

URL = "https://www.saucedemo.com/"
LOGIN1 = "standard_user"
PASSWORD = "secret_sauce"
RESULT = ".app_logo"
INCOR_PASS = "QWERTY12345"
BLOCKED_USER = "locked_out_user"


class LoginPage:
    def __init__(self, page: Page):
        self.page = page


    def open(self) -> object:
        self.page.goto(URL)


    def input_login(self):
        login = self.page.locator("#user-name")
        login.fill(LOGIN1)

    def input_password(self):
        password = self.page.locator("#password")
        password.fill(PASSWORD)


    def click_button_enter(self):
        button = self.page.locator("#login-button")
        button.click()
        time.sleep(3)


    def expected_main_page(self):
        result = self.page.locator(RESULT)
        expect(result).to_have_text("Swag Labs")
        time.sleep(1)



    def incorrect_password(self):
        password = self.page.locator("#password")
        password.fill(INCOR_PASS)


    def expected_allert(self):
        alert = self.page.get_by_text("Epic sadface: Username and password do not match any user in this service")
        expect(alert).to_be_visible()

    def logout_main_page(self):
        burger_menu = self.page.locator("#react-burger-menu-btn")
        burger_menu.click()
        logout = self.page.locator("#logout_sidebar_link")
        logout.click()
        string_login_page = self.page.get_by_text("Accepted usernames are")
        expect(string_login_page).to_be_visible()

    def input_with_empty_fields(self):
        allert = self.page.get_by_text("Epic sadface: Username is required")
        expect(allert).to_be_visible()


    def empty_password(self):
        allert = self.page.get_by_text("Epic sadface: Password is required")
        expect(allert).to_be_visible()



    def blocked_user_input(self):
        login = self.page.locator("#user-name")
        login.fill(BLOCKED_USER)

    def blocked_user(self):

        allert = self.page.get_by_text("Epic sadface: Sorry, this user has been locked out.")
        expect(allert).to_be_visible()



