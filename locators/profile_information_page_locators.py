from selenium.webdriver.common.by import By


class ProfileInformationPageLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]")
    ORDERS_HISTORY_BUTTON = (By.XPATH, ".//a[contains(text(), 'История заказов')]")
    LAST_ORDER_IN_HISTORY = (By.XPATH, "//li[last()][contains(@class,'OrderHistory_listItem__2x95r mb-6')][1]/a/div/p[1]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

