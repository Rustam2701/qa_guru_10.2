import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def size_browser():
    browser.config.window_width = 1200
    browser.config.height = 1200
    yield

    browser.quit()

