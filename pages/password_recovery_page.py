from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
import allure


class PasswordRecoveryPage(BasePage):


    @allure.step('Ввести почту в разделе восстановления пароля')
    def enter_email(self, email):
        enter_email = self.enter_data(PasswordRecoveryPageLocators.ENTER_EMAIL_FIELD, email)
        return enter_email


    @allure.step('Нажать на кнопку подтверждения после ввода почты в разделе восстановления пароля')
    def click_email_submit_button(self):
        click_email_submit_button = self.click_element(PasswordRecoveryPageLocators.EMAIL_SUBMIT_BUTTON)
        return click_email_submit_button


    @allure.step('Кликнуть на значок "Показать пароль""')
    def click_enter_password_field_eye(self):
        click_enter_password_field_eye = self.click_element(PasswordRecoveryPageLocators.ENTER_PASSWORD_FIELD_EYE)
        return click_enter_password_field_eye


