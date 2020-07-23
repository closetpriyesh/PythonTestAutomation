import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    try:
        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path=r'resources\chromedriver.exe')
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path=r'resources\geckodriver.exe')
        else:
            raise UnboundLocalError
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        driver.implicitly_wait(3)
        request.cls.driver = driver
        yield
        driver.close()
        return driver
    except UnboundLocalError as ule:
        print("Please enter the correct browser name")
        print(ule)
