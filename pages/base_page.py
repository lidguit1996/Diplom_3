from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from data import Urls



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(Urls.BURGERS_MAIN)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_element_to_click(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        click_element = self.wait_element_to_click(locator)
        return click_element.click()

    def enter_data(self, locator, data):
        enter_data = self.wait_and_find_element(locator)
        return enter_data.send_keys(data)


    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def transfer_element(self, driver, locator_element, locator_target):
        element = self.wait_element_to_click(locator_element)
        target = self.wait_element_to_click(locator_target)
        transfer = ActionChains(driver)
        transfer.drag_and_drop(element, target)
        return transfer.perform()

    def get_current_url(self, driver):
        return driver.current_url

