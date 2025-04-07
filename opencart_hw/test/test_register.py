import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators = [
    (By.ID, "input-firstname"),
    (By.ID, "input-lastname"),
    (By.ID, "input-email"),
    (By.ID, "input-password"),
    (By.NAME, "agree"),
]

@pytest.mark.parametrize("locator", locators)
def test_register_elements(browser, base_url, locator):
    browser.get(base_url + "/index.php?route=account/register")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))