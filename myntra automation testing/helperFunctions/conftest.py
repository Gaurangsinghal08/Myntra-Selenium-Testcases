import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.homepageLocators import *
driver = webdriver.Chrome()
"""
fixture related to helper function
"""


@pytest.fixture(scope="class")
def helper_function():
    driver.get("https://www.myntra.com/")
    driver.maximize_window()
    yield


"""
fixture related to login and logout
"""


@pytest.fixture(scope="class")
def login_and_logout():
    driver.implicitly_wait(45)
    driver.implicitly_wait(45)
    driver.find_element(by=By.XPATH, value=profile_button).click()
    driver.find_element(by=By.XPATH, value=signup_button).click()
    driver.find_element(by=By.XPATH, value=mobile_number).send_keys("6376351248")
    driver.find_element(by=By.XPATH, value=continue_button).click()
    driver.find_element(by=By.XPATH, value=log_in_using_password).click()
    driver.find_element(by=By.XPATH, value=password).send_keys("Gaurang1#")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, final_login_button))
    )
    driver.find_element(by=By.XPATH, value=final_login_button).click()
    import time
    time.sleep(5)

