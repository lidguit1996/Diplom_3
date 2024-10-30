from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    LOGIN_LINK_IN_FORGOT_PASSWORD_WINDOW = (By.LINK_TEXT, "Войти")
    ENTER_EMAIL_FIELD = (By.XPATH, ".//input[contains(@class,'text input__textfield text_type_main-default')]")
    EMAIL_SUBMIT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Восстановить')]")
    ENTER_PASSWORD_FIELD = (By.XPATH, ".//input[contains(@class,'text input__textfield text_type_main-default')]")
    ENTER_PASSWORD_FIELD_EYE = (By.XPATH, ".//div[contains(@class,'input__icon input__icon-action')]")
    ENTER_PASSWORD_FIELD_ACTIVE = (By.XPATH, "//label[contains(@class,'input__placeholder text noselect text_type_main-default input__placeholder-focused')]")
