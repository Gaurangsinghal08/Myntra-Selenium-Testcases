from helperFunctions.ProfilePageFunctions import *
from locators.ProfilePageLocators import *
"""
Author: Gaurang Singhal
Date Created: 25/03/2022
Date Modified: 06/04/2022
Test Case related to profile page
"""


@pytest.mark.usefixtures("helper_function", "login_and_logout")
class TestProfilePage:
    def test_user_is_able_to_go_on_profile_page(self):
        profilepage = Profilepage()
        profilepage.go_to_profile_page()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, profile_name_text))
        )
        assert "Account" in profilepage.get_element_text(profile_name_text), "profile page missing"

    def test_user_is_able_to_go_on_overview_page(self):
        profilepage = Profilepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, overview_button))
        )
        driver.find_element(by=By.XPATH, value=overview_button).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, overview_text))
        )
        assert "gaurangsinghal1122@gmail.com" in profilepage.get_element_text(overview_text)

    def test_user_is_able_to_see_his_orders(self):
        profilepage = Profilepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, orders_button))
        )
        driver.find_element(by=By.XPATH, value=orders_button).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, orders_text))
        )
        assert "All Orders" in profilepage.get_element_text(orders_text)

    def test_user_is_able_to_use_myntra_credit(self):
        profilepage = Profilepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, myntra_credit_button))
        )
        driver.find_element(by=By.XPATH, value=myntra_credit_button).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, myntra_credit_text))
        )
        assert "A QUICK AND CONVENIENT" in profilepage.get_element_text(myntra_credit_text)

    def test_user_is_use_myn_cash(self):
        profilepage = Profilepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, myn_cash))
        )
        driver.find_element(by=By.XPATH, value=myn_cash).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, myn_cash_text))
        )
        assert "MYNCASH" in profilepage.get_element_text(myn_cash_text)

    def test_user_can_see_saved_address(self):
        profilepage = Profilepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, addresses_button))
        )
        driver.find_element(by=By.XPATH, value=addresses_button).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, addresses_text))
        )
        assert "Saved" in profilepage.get_element_text(addresses_text)

    def test_user_can_go_to_homepage(self):
        profilepage = Profilepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, myntra_home_button_icons))
        )
        driver.find_element(by=By.XPATH, value=myntra_home_button_icons).click()
        driver.execute_script("window.scrollTo(0, 5500)")
        assert "100% ORIGINAL" in profilepage.get_element_text(homepage_verification_text), "we are not in homepage"
        driver.quit()
