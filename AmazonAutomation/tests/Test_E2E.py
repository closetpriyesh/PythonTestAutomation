import pytest

from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):

    @pytest.mark.end_to_end
    def test_e2e_functionality(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        product_page = ProductPage(self.driver)
        home_page.get_search_box().send_keys("laptop")
        home_page.get_search_icon().click()
        search_page.get_first_item_price_element().click()
        main_window = self.driver.window_handles[0]
        child_window = self.driver.window_handles[1]
        self.driver.switch_to.window(child_window)
        assert product_page.get_add_to_card_button().is_displayed()
        assert product_page.get_buy_now_button().is_displayed()
        assert "buy now" in product_page.get_buy_now_button().find_element_by_xpath("parent::span/span").text.lower()
        assert "add to cart" in product_page.get_add_to_card_button().get_attribute('value').lower()
        self.driver.close()
        self.driver.switch_to.window(main_window)




