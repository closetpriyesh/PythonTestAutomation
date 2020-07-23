import pytest

from pages.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    @pytest.mark.smoke
    def test_search_button_functionality(self, get_data):
        home_page = HomePage(self.driver)
        home_page.get_search_box().send_keys(get_data["keyword"])
        home_page.get_search_icon().click()
        assert get_data["keyword"] in self.driver.title

    @pytest.fixture(params=HomePageData.test_home_page_data)
    def get_data(self, request):
        return request.param

