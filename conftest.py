from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page

# Logins
# 1.standard_user
# 2.locked_out_user
# 3.problem_user
# 4.performance_glitch_user
# 5.error_user
# 6.visual_user

# all_password
# secret_sauce
