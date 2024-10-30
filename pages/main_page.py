from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Личный кабинет" на главной странице')
    def click_account_button(self):
        click_registration_button = self.click_element(MainPageLocators.ACCOUNT_BUTTON)
        return click_registration_button

