from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    LAST_ORDER_IN_FEED = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem__2x95r mb-6')][1]/a/div/p")
    ORDER_DETAILS_MODAL_WINDOW = (By.XPATH, "//section[contains(@class,'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]")
    ORDERS_ALL_TIME_COUNTER = (By.XPATH, "//div[2]/p[contains(@class,'OrderFeed_number__2MbrQ text text_type_digits-large')]")
    ORDERS_PER_DAY_COUNTER = (By.XPATH, "//div[3]/p[contains(@class,'OrderFeed_number__2MbrQ text text_type_digits-large')]")
    ORDER_NUMBER_IN_WORK = (By.XPATH, "//ul[2]/li[contains(@class,'text text_type_digits-default mb-2')]")


