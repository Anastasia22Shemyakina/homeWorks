import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators = [
    (By.TAG_NAME, "h1"),
    (By.CLASS_NAME, "price"),
    (By.ID, "button-cart"),
    (By.ID, "input-quantity"),
    (By.ID, "content"),
]

@pytest.mark.parametrize("locator", locators)
def test_product_elements(browser, base_url, locator):
    browser.get(base_url + "/index.php?route=product/product&product_id=40")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))