from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_main_page import AccountMainPage
from pages.orders_feed_page import OrdersFeedPage
from locators.account_main_page_locators import AccountMainPageLocators
from data import Credentions, Prices
import allure


class TestConstructor:


    @allure.title('Проверка работоспособности кнопки "Конструктора"')
    @allure.description('Авторизуемся в личном кабинете, переходим в ленту заказов, далее обратно в конструктор')
    def test_click_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.go_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.go_constructor()
        assert account_main_page.wait_and_find_element(AccountMainPageLocators.SUBMIT_ORDER_BUTTON).is_displayed



    @allure.title('Проверка открытия окна деталей ингредиента')
    @allure.description('Авторизуемся в личном кабинете, кликаем по ингредиенту в конструкторе, проверяем появление деталей')
    def test_open_ingredient_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.open_ingredient_window(AccountMainPageLocators.CRATER_BREAD_ICON)
        assert account_main_page.wait_and_find_element(AccountMainPageLocators.INGREDIENT_MODAL_WINDOW).is_displayed()


    @allure.title('Проверка закрытия окна деталей ингредиента')
    @allure.description('Авторизуемся в личном кабинете, кликаем по ингредиенту в конструкторе, кликаем по кнопке закрытия')
    def test_close_ingredient_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.open_ingredient_window(AccountMainPageLocators.CRATER_BREAD_ICON)
        account_main_page.close_ingredient_window()
        assert account_main_page.find_ingredient_window_after_closing() == "Модальное окно закрыто"


    @allure.title('Проверка перемещения ингредиента в конструктор')
    @allure.description('Авторизуемся в личном кабинете, перетаскиваем ингредиент в конструктор бургера')
    def test_constructor_put_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        start_price = account_main_page.find_order_price()
        account_main_page.put_ingredient_to_constructor_field(AccountMainPageLocators.CRATER_BREAD_ICON)
        order_price = account_main_page.find_order_price()
        assert start_price < order_price and order_price == Prices.CRATER_BREAD*2


    @allure.title('Проверка флоу заказа авторизованного пользователя')
    @allure.description('Авторизуемся в личном кабинете, собираем бургер, оформляем заказ')
    def test_signed_user_order_successful(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.put_ingredient_to_constructor_field(AccountMainPageLocators.CRATER_BREAD_ICON)
        account_main_page.submit_order()
        assert account_main_page.wait_and_find_element(AccountMainPageLocators.ORDER_SUBMIT_MODAL_WINDOW_ACTIVE).is_displayed()












