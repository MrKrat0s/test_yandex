import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def open_brouser():
    driver = webdriver.Chrome(executable_path="chromedriver\\chromedriver.exe")
    yield driver
    driver.quit()

