from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_main_page import AccountMainPage
from pages.profile_information_page import ProfileInformationPage
from locators.profile_information_page_locators import ProfileInformationPageLocators
from locators.login_page_locators import LoginPageLocators
from data import Urls, Credentions
import allure


class TestAccount:

    @allure.title('Проверка перехода в информацию о профиле')
    @allure.description('Авторизуемся в личном кабинете и переходим в информацию о профиле')
    def test_login_and_go_profile_information(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.go_profile_information()
        profile_information_page = ProfileInformationPage(driver)
        assert profile_information_page.wait_and_find_element(ProfileInformationPageLocators.LOGOUT_BUTTON).is_displayed()


    @allure.title('Проверка перехода в историю заказов')
    @allure.description('Авторизуемся в личном кабинете, переходим информацию о профиле, далее в историю заказов')
    def test_go_orders_history(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.go_profile_information()
        profile_information_page = ProfileInformationPage(driver)
        profile_information_page.go_orders_history()
        assert profile_information_page.get_current_url(driver) == Urls.ORDERS_HISTORY


    @allure.title('Проверка выхода из профиля')
    @allure.description('Авторизуемся в личном кабинете и переходим в информацию о профиле, кликаем по кнопке выхода')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Credentions.CREATED_USER_1_EMAIL, Credentions.CREATED_USER_1_PASSWORD)
        account_main_page = AccountMainPage(driver)
        account_main_page.go_profile_information()
        profile_information_page = ProfileInformationPage(driver)
        profile_information_page.logout()
        assert login_page.wait_and_find_element(LoginPageLocators.SUBMIT_BUTTON).is_displayed()

