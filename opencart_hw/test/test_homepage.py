import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators = [
    (By.ID, "logo"),
    (By.NAME, "search"),
    (By.LINK_TEXT, "Desktops"),
    (By.CSS_SELECTOR, ".navbar-nav"),
    (By.ID, "wishlist-total"),
]

@pytest.mark.parametrize("locator", locators)
def test_homepage_elements(browser, base_url, locator):
    browser.get(base_url)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))