import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_main_page import AccountMainPage
from pages.orders_feed_page import OrdersFeedPage
from locators.orders_feed_page_locators import OrdersFeedLocators
from pages.profile_information_page import ProfileInformationPage
from locators.account_main_page_locators import AccountMainPageLocators
from data import Urls, Credentions
import allure


class TestOrdersFeed:


    @allure.title('Проверка открытия деталей заказа')
    @allure.description('Авторизуемся в личном кабинете, преходим в историю заказов, кликаем по заказу')
    def test_open_order_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BURGERS_MAIN)
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.go_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_order_details_window(OrdersFeedLocators.LAST_ORDER_IN_FEED)
        assert orders_feed_page.wait_and_find_element(OrdersFeedLocators.ORDER_DETAILS_MODAL_WINDOW).is_displayed()



    @allure.title('Проверяем отображение заказа из "Истории" в ленте заказов')
    @allure.description('Авторизуемся в личном кабинете, совершаем заказ, переходим в историю заказов, получаем информацию о последнем заказе, переходим в ленту заказов, проверяем, есть ли там заказ из истории')
    def test_order_from_history_displayed_in_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BURGERS_MAIN)
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        time.sleep(1)
        account_main_page.put_ingredient_to_constructor_field(driver, AccountMainPageLocators.CRATER_BREAD_ICON)
        account_main_page.submit_order()
        time.sleep(1)
        account_main_page.close_order_window()
        account_main_page.go_profile_information()
        profile_information_page = ProfileInformationPage(driver)
        profile_information_page.go_orders_history()
        my_order_in_history = profile_information_page.get_last_my_order_in_history()
        profile_information_page.go_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        my_order_in_feed = orders_feed_page.get_last_my_order_in_feed()
        assert my_order_in_history == my_order_in_feed



    @allure.title('Проверка отображения нового заказа в количесвте заказов за все время')
    @allure.description('Авторизуемся в личном кабинете, проверяем количество заказов за все время в ленте заказов, создаем новый заказ, проверяем, увеличилось ли количество заказов за все время в ленте')
    def test_order_all_time_counter_change_after_my_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BURGERS_MAIN)
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.go_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        orders_count_before_my_order = orders_feed_page.get_orders_all_time_count()
        orders_feed_page.go_constructor()
        time.sleep(1)
        account_main_page.put_ingredient_to_constructor_field(driver, AccountMainPageLocators.CRATER_BREAD_ICON)
        account_main_page.submit_order()
        time.sleep(1)
        account_main_page.close_order_window()
        account_main_page.go_orders_feed()
        time.sleep(1)
        orders_count_after_my_order = orders_feed_page.get_orders_all_time_count()
        assert orders_count_after_my_order > orders_count_before_my_order


    @allure.title('Проверка отображения нового заказа в количесвте заказов за день')
    @allure.description('Авторизуемся в личном кабинете, проверяем количество заказов за все время в ленте заказов, создаем новый заказ, проверяем, увеличилось ли количество заказов за день в ленте')
    def test_order_per_day_counter_change_after_my_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BURGERS_MAIN)
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.go_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        orders_count_before_my_order = orders_feed_page.get_orders_per_day_count()
        orders_feed_page.go_constructor()
        time.sleep(1)
        account_main_page.put_ingredient_to_constructor_field(driver, AccountMainPageLocators.CRATER_BREAD_ICON)
        account_main_page.submit_order()
        time.sleep(1)
        account_main_page.close_order_window()
        account_main_page.go_orders_feed()
        time.sleep(1)
        orders_count_after_my_order = orders_feed_page.get_orders_per_day_count()
        assert orders_count_after_my_order > orders_count_before_my_order


    @allure.title('Проверка отображения нового заказа на табло "В работе" в ленте заказов')
    @allure.description('Авторизуемся в личном кабинете, создаем новый заказ, прехеодим в ленту заказов, проверяем, появился ли номер заказа на табло "В работе"')
    def test_my_new_order_dsipayed_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BURGERS_MAIN)
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        time.sleep(1)
        account_main_page.put_ingredient_to_constructor_field(driver, AccountMainPageLocators.CRATER_BREAD_ICON)
        time.sleep(1)
        account_main_page.submit_order()
        time.sleep(2)
        my_order_number = account_main_page.get_my_order_number()
        account_main_page.close_order_window()
        account_main_page.go_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        time.sleep(2)
        order_number_in_work = orders_feed_page.get_order_number_in_work()
        assert order_number_in_work == my_order_number




