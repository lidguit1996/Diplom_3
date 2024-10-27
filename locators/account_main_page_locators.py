from selenium.webdriver.common.by import By


class AccountMainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    CRATER_BREAD_ICON = (By.XPATH, ".//img[@alt = 'Краторная булка N-200i']")
    INGREDIENT_MODAL_WINDOW = (By.XPATH, "//section[contains(@class,'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]")
    INGREDIENT_MODAL_WINDOW_CLOSE_BUTTON = (By.XPATH, "//*[@id='root']/div/section[1]/div[1]/button")
    CONSTRUCTOR_FIELD = (By.XPATH, "//span[contains(text(),'Перетяните булочку сюда (верх)')]")
    ORDER_PRICE_COUNTER = (By.XPATH, "//p[contains(@class,'text text_type_digits-medium mr-3')]")
    ORDER_SUBMIT_MODAL_WINDOW_ACTIVE = (By.XPATH, "//section[contains(@class,'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]")
    MY_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
    ORDER_MODAL_WINDOW_CLOSE_BUTTON = (By.XPATH, "//div/section[1]/div[1]/button")




