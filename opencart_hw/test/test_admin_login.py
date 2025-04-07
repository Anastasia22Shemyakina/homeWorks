import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators = [
    (By.ID, "input-username"),
    (By.ID, "input-password"),
    (By.TAG_NAME, "button"),
    (By.TAG_NAME, "footer"),
    (By.ID, "alert"),  # заменили проблемный селектор
]

@pytest.mark.parametrize("locator", locators)
def test_admin_login_elements(browser, base_url, locator):
    browser.get(base_url + "/administration")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))