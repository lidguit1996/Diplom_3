from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = (By.LINK_TEXT, "Восстановить пароль")

    ENTER_EMAIL_FIELD = (By.XPATH, ".//input[@name = 'name']")
    ENTER_PASSWORD_FIELD = (By.XPATH, ".//input[@name = 'Пароль']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')]")


