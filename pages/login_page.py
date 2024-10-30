from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):


    @allure.step('Кликнуть по кнопке восстановления пароля')
    def click_password_recovery_button(self):
        click_password_recovery_button = self.click_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)
        return click_password_recovery_button


    @allure.step('Ввести почту для авторизации')
    def enter_email(self, email):
        enter_email = self.enter_data(LoginPageLocators.ENTER_EMAIL_FIELD, email)
        return enter_email


    @allure.step('Ввести пароль для авторизации')
    def enter_password(self, password):
        enter_password = self.enter_data(LoginPageLocators.ENTER_PASSWORD_FIELD, password)
        return enter_password


    @allure.step('Кликнуть по кнопке подтверждения входа')
    def submit_enter(self):
        submit_enter = self.click_element(LoginPageLocators.SUBMIT_BUTTON)
        return submit_enter


    @allure.step('Авторизоваться на странице авторизации')
    def login_account(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.submit_enter()

