from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    first_item_text_element = (By.XPATH, "//*[contains(@class,'sg-col-inner')]//h2")
    first_item_price_element = (By.CSS_SELECTOR, "span[class='a-price-whole']")
    searched_text = (By.CSS_SELECTOR, "span[class='a-color-state a-text-bold']")

    def get_first_item_text_element(self):
        self.logger.info("Attempt to get first item text element")
        return self.driver.find_element(*SearchPage.first_item_text_element)

    def get_first_item_price_element(self):
        self.logger.info("Attempt to get first item price element")
        return self.driver.find_element(*SearchPage.first_item_price_element)

    def get_searched_text(self):
        self.logger.info("Attempt to get searched text")
        return self.driver.find_element(*SearchPage.searched_text)




