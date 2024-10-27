from pages.base_page import BasePage
from locators.orders_feed_page_locators import OrdersFeedLocators
import allure


class OrdersFeedPage(BasePage):


    @allure.step('Перейти в "Конструктор"')
    def go_constructor(self):
        go_constructor = self.click_element(OrdersFeedLocators.CONSTRUCTOR_BUTTON)
        return go_constructor


    @allure.step('Перейти в конструктор')
    def open_order_details_window(self, locator):
        open_order_details = self.click_element(locator)
        return open_order_details


    @allure.step('Узнать номер последнего заказа в ленте')
    def get_last_my_order_in_feed(self):
        get_last_my_order_in_feed = self.wait_and_find_element(OrdersFeedLocators.LAST_ORDER_IN_FEED)
        return get_last_my_order_in_feed.text


    @allure.step('Узнать количество заказов за всё время')
    def get_orders_all_time_count(self):
        get_orders_all_time_count = self.wait_and_find_element(OrdersFeedLocators.ORDERS_ALL_TIME_COUNTER)
        return int(get_orders_all_time_count.text)


    @allure.step('Узнать количество заказов за день')
    def get_orders_per_day_count(self):
        get_orders_per_day_count = self.wait_and_find_element(OrdersFeedLocators.ORDERS_PER_DAY_COUNTER)
        return int(get_orders_per_day_count.text)


    @allure.step('Узнать номер заказа, который изготавливается')
    def get_order_number_in_work(self):
        get_order_number_in_work = self.wait_and_find_element(OrdersFeedLocators.ORDER_NUMBER_IN_WORK)
        return int(get_order_number_in_work.text)



