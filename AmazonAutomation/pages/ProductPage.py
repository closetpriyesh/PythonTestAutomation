from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    add_to_card_button = (By.ID, "add-to-cart-button")
    buy_now_button = (By.XPATH, "//*[@id='buy-now-button']")

    def get_add_to_card_button(self):
        self.logger.info("Attempt to get 'add to cart' button")
        return self.driver.find_element(*ProductPage.add_to_card_button)

    def get_buy_now_button(self):
        self.logger.info("Attempt to get 'buy now' button")
        return self.driver.find_element(*ProductPage.buy_now_button)


