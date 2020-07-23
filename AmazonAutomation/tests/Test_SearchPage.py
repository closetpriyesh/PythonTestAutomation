import pytest

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestSearchPage(BaseClass):

    @pytest.mark.smoke
    def test_e2e_functionality(self):
        home_page = HomePage(self.driver)
        search_page = SearchPage(self.driver)
        home_page.get_search_box().send_keys("laptop")
        home_page.get_search_icon().click()
        assert "laptop" in search_page.get_first_item_text_element().text.lower()
        assert "laptop" in search_page.get_searched_text().text
