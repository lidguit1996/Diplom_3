from pages.base_page import BasePage
from locators.profile_information_page_locators import ProfileInformationPageLocators
import allure


class ProfileInformationPage(BasePage):


    @allure.step('Нажать на кнопку выхода из аккаунта')
    def logout(self):
        logout = self.click_element(ProfileInformationPageLocators.LOGOUT_BUTTON)
        return logout


    @allure.step('Перейти в историю заказов')
    def go_orders_history(self):
        go_orders_history = self.click_element(ProfileInformationPageLocators.ORDERS_HISTORY_BUTTON)
        return go_orders_history


    @allure.step('Перейти в ленту заказов')
    def go_orders_feed(self):
        go_orders_feed = self.click_element(ProfileInformationPageLocators.ORDERS_FEED_BUTTON)
        return go_orders_feed


    @allure.step('Узнать свой последний заказ в истории заказов')
    def get_last_my_order_in_history(self):
        get_last_my_order_in_history = self.wait_and_find_element(ProfileInformationPageLocators.LAST_ORDER_IN_HISTORY)
        return get_last_my_order_in_history.text





