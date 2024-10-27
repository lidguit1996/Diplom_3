import allure

from pages.base_page import BasePage
from locators.account_main_page_locators import AccountMainPageLocators


class AccountMainPage(BasePage):

    @allure.step('Переход в "Профиль"')
    def go_profile_information(self):
        go_profile_information = self.click_element(AccountMainPageLocators.ACCOUNT_BUTTON)
        return go_profile_information


    @allure.step('Переход в ленту заказов')
    def go_orders_feed(self):
        go_orders_feed = self.click_element(AccountMainPageLocators.ORDERS_FEED_BUTTON)
        return go_orders_feed


    @allure.step('Открыть информацию об ингредиенте')
    def open_ingredient_window(self, locator):
        open_ingredient_window = self.click_element(locator)
        return open_ingredient_window


    @allure.step('Закрыть информацию об ингредиенте')
    def close_ingredient_window(self):
        close_ingredient_window = self.click_element(AccountMainPageLocators.INGREDIENT_MODAL_WINDOW_CLOSE_BUTTON)
        return close_ingredient_window


    @allure.step('Попытаться найти окно ингредиента после закрытия')
    def find_ingredient_window_after_closing(self):
        try:
            self.wait_and_find_element(AccountMainPageLocators.INGREDIENT_MODAL_WINDOW)
        except Exception:
            result = "Модальное окно закрыто"
        return result


    @allure.step('Переместить ингредиент в поле создания бургера')
    def put_ingredient_to_constructor_field(self, driver, ingredient):
        put_ingredient_to_constructor_field = self.transfer_element(driver, ingredient, AccountMainPageLocators.CONSTRUCTOR_FIELD)
        return put_ingredient_to_constructor_field



    @allure.step('Узнать стоимость своего заказа')
    def find_order_price(self):
        find_order_price = self.wait_and_find_element(AccountMainPageLocators.ORDER_PRICE_COUNTER)
        return int(find_order_price.text)


    @allure.step('Кликнуть по кнопке оформления заказа')
    def submit_order(self):
        submit_order = self.click_element(AccountMainPageLocators.SUBMIT_ORDER_BUTTON)


    @allure.step('Узнать свой номер заказа из модального окна заказа')
    def get_my_order_number(self):
        my_order_number = self.wait_and_find_element(AccountMainPageLocators.MY_ORDER_NUMBER)
        return int(my_order_number.text)


    @allure.step('Закрыть модальное окно с номером оформленного заказа ')
    def close_order_window(self):
        close_order_window = self.click_element(AccountMainPageLocators.ORDER_MODAL_WINDOW_CLOSE_BUTTON)
        return close_order_window
