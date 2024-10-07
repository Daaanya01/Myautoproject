from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time
import pytest



SORTINGMENU = "product_sort_container"
PRICE_LOW_TO_HIGH = "Price (low to high)"
PRICE_HIGH_TO_LOW = "Price (high to low)"
NAME_A_TO_Z = "Name (A to Z)"
NAME_Z_TO_A = "Name (Z to A)"
#КНОПКИ ДЛЯ ДОБАВЛЕНИЯ ТОАВРОВ В КОРЗИНУ
BACKPACK = '#add-to-cart-sauce-labs-backpack'
BIKE = "#add-to-cart-sauce-labs-bike-light"
T_SHIRT = "#add-to-cart-sauce-labs-bolt-t-shirt"
JACKET = "#add-to-cart-sauce-labs-fleece-jacket"
ONESIE = "#add-to-cart-sauce-labs-onesie"

#КНОПКИ УДАЛЕНИЯ ТОВАРОВ ИЗ КОРЗИНЫ
DEL_BACKPACK = "#remove-sauce-labs-backpack"
DEL_BIKE = "#remove-sauce-labs-bike-light"
DEL_T_SHIRT = "#remove-sauce-labs-bolt-t-shirt"
DEL_JACKET = "#remove-sauce-labs-fleece-jacket"
DEL_ONESIE = "#remove-sauce-labs-onesie"
#КНОПККА ОФОРМЛЕНИЯ ЗАКАЗА
CHECKOUT = "#checkout"

#Кнопка финиша оформления заказа
BUTTON_FINISH = "#finish"


class MainPage:
    def __init__(self, page: Page):
        self.page = page


    def open_sorting(self):
        sorting_menu = self.page.locator(SORTINGMENU)
        sorting_menu.click()


    def sorting_by_price_low_to_high(self):
        sorting_menu = self.page.get_by_text(PRICE_LOW_TO_HIGH)
        sorting_menu.click()

    #Надо думать как проверять сортивровку , пока вообще не понимаю (По коду, тот что сверху)




    def add_one_product_in_basket(self):
        add_button = self.page.locator(BACKPACK)
        add_button.click()
        int_basket = self.page.locator('.shopping_cart_badge')
        expect(int_basket).to_have_text('1')



    def go_to_basket(self):
        go_basket = self.page.locator(".shopping_cart_link")
        go_basket.click()


    def delete_product_from_basket(self):
        delete = self.page.locator(DEL_BACKPACK)
        delete.click()
        int_basket = self.page.locator('.shopping_cart_badge')
        expect(int_basket).not_to_be_visible()






    def add_four_product_in_basket(self):
        add_backpack = self.page.locator(BACKPACK)
        add_backpack.click()
        add_bike = self.page.locator(BIKE)
        add_bike.click()
        add_tshirt = self.page.locator(T_SHIRT)
        add_tshirt.click()
        add_jacket = self.page.locator(JACKET)
        add_jacket.click()

    def making_an_oreder(self):
        # Переход на страницу оформления заказа
        checkout = self.page.locator(CHECKOUT)
        checkout.click()
        #Проверка факта перехода (цепляемся к заголовку)
        checkout_info = self.page.locator('.title')
        expect(checkout_info).to_have_text("Checkout: Your Information")

        #Ввод данных для оформления и переход на страницу овервью
        firts_name = self.page.locator("#first-name")
        firts_name.fill("Ivan")
        last_name = self.page.locator("#last-name")
        last_name.fill("Ivanov")
        zip = self.page.locator("#postal-code")
        zip.fill("14000012")
        button_continue = self.page.locator("#continue")
        button_continue.click()

        #Проверка перехода на оверьвю (цепляемся к заголовку)
        check_overview = self.page.get_by_text("Checkout: Overview")
        expect(check_overview).to_be_visible()

        #Оформление и прверка успешного оформления
        button_finish = self.page.locator(BUTTON_FINISH)
        button_finish.click()
        finish_string = self.page.get_by_text("Thank you for your order!")
        expect(finish_string).to_be_visible()

    # Использование опции reset_app_state
    def using_options_reset_app_state(self):
        menu = self.page.locator('#react-burger-menu-btn')
        menu.click()
        reset = self.page.locator('#reset_sidebar_link')
        reset.click()

        #Проверка отсутствия товаров в корзине
    def expected_basket(self):
        int_basket = self.page.locator('.shopping_cart_badge')
        expect(int_basket).not_to_be_visible()





