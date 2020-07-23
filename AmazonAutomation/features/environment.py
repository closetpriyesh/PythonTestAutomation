from selenium import webdriver

from pages.HomePage import HomePage
from pages.ProductPage import ProductPage
from pages.SearchPage import SearchPage


def before_all(context):
    context.driver = webdriver.Chrome(executable_path=r'resources\chromedriver.exe')
    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    context.home_page = HomePage(context.driver)
    context.search_page = SearchPage(context.driver)
    context.product_page = ProductPage(context.driver)
