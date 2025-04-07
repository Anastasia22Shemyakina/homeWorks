import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators = [
    (By.CSS_SELECTOR, ".product-thumb"),
    (By.CSS_SELECTOR, ".product-thumb h4"),  # исправили тут
    (By.ID, "input-sort"),
    (By.ID, "input-limit"),
    (By.CSS_SELECTOR, ".list-group"),
]

@pytest.mark.parametrize("locator", locators)
def test_catalog_elements(browser, base_url, locator):
    browser.get(base_url + "/index.php?route=product/category&path=20")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))