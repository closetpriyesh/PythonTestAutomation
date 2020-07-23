from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    search_box = (By.ID, "twotabsearchtextbox")
    search_icon = (By.XPATH, "//input[@value='Go']")

    def get_search_box(self):
        self.logger.info("Attempt to get search box element")
        return self.driver.find_element(*HomePage.search_box)

    def get_search_icon(self):
        self.logger.info("Attempt to get search icon element")
        return self.driver.find_element(*HomePage.search_icon)





