from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from data import Credentions
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
import allure


class TestPasswordRecovery:

    @allure.title('Проверка открытия страницы восстановления пароля')
    @allure.description('Переходим на страницу авторизации, затем на страницу восстановления пароля')
    def test_recovery_password_page_open(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        assert password_recovery_page.wait_and_find_element(PasswordRecoveryPageLocators.ENTER_EMAIL_FIELD).is_displayed()


    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    @allure.description('Переходим на страницу авторизации, затем на страницу сброса пароля, вводим почту, кликаем по кнопке "Восстановить"')
    def test_enter_email_and_submit_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.enter_email(Credentions.CREATED_USER_2_EMAIL)
        password_recovery_page.click_email_submit_button()
        assert password_recovery_page.wait_and_find_element(PasswordRecoveryPageLocators.ENTER_PASSWORD_FIELD).is_displayed()

    @allure.title('Проверка подсветки поля пароля при нажатии на значок "Показать пароль"')
    @allure.description('Переходим на страницу авторизации, затем на страницу сброса пароля, вводим почту, кликаем по кнопке "Восстановить", нажимаем на значок "глаза" поля ввода пароля')
    def test_enter_password_field_active(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.enter_email(Credentions.CREATED_USER_2_EMAIL)
        password_recovery_page.click_email_submit_button()
        password_recovery_page.click_enter_password_field_eye()
        assert password_recovery_page.wait_and_find_element(PasswordRecoveryPageLocators.ENTER_PASSWORD_FIELD_ACTIVE).is_displayed()


