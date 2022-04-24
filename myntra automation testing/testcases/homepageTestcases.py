from selenium.webdriver import Keys
from helperFunctions.homepageFunctions import *
"""
Author: Gaurang Singhal
Date Created: 25/03/2022
Date Modified: 06/04/2022
Test Case related to homepage
"""


class TestHomepage:

    @pytest.mark.usefixtures("helper_function")
    def test_all_homepage_button_are_visible(self):
        profile_button1 = driver.find_element(by=By.XPATH, value=homepageLocators.profile_button)
        assert profile_button1.is_displayed(), "profile button missing"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.wishlist_button))
        )
        wishlist_button1 = driver.find_element(by=By.XPATH, value=homepageLocators.wishlist_button)
        assert wishlist_button1.is_displayed(), "wishlist button missing"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.bag_buuton))
        )
        bag_button1 = driver.find_element(by=By.XPATH, value=homepageLocators.bag_buuton)
        assert bag_button1.is_displayed(), "bag button missing"
        profile_button1.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.login_button))
        )
        login_button1 = driver.find_element(by=By.XPATH, value=homepageLocators.login_button)
        assert login_button1.is_displayed(), "login button missing"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_see_his_cart(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.cart_button))
        )
        cart_button1 = driver.find_element(by=By.XPATH, value=homepageLocators.cart_button)
        assert cart_button1.is_displayed(), "cart button missing"
        cart_button1.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.add_items_from_wishlist))
        )
        add_items_from_wishlist1 = driver.find_element(by=By.XPATH, value=homepageLocators.add_items_from_wishlist)
        assert add_items_from_wishlist1.is_displayed(), "wishlist is missing"
        add_items_from_wishlist1.click()
        assert "wishlist" in driver.current_url, "we are not in wishlist page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_can_access_frequently_asked_questions(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.profile_button))
        )
        homepage = Homepage()
        driver.execute_script("window.scrollTo(0, 5500)")
        assert "100% ORIGINAL" in homepage.get_element_text(
            homepageLocators.homepage_verification_text), "we are not in homepage"
        homepage.click_profile_button()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.contact_us))
        )
        homepage.click_contact_button()
        assert "HELP CENTER" in homepage.get_element_text(
            homepageLocators.help_center_text), "We are not in contact us page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.faq))
        )
        driver.find_element(by=By.XPATH, value=homepageLocators.faq).click()
        assert "Frequently" in homepage.get_element_text(homepageLocators.faq_text)

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_switch_categories(self):
        homepage = Homepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.men_button))
        )
        driver.find_element(by=By.XPATH, value=homepageLocators.men_button).click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.men_page_text))
        )
        assert "ONLINE SHOPPING FOR MEN" in homepage.get_element_text(homepageLocators.men_page_text)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.kids_option))
        )
        driver.find_element(by=By.XPATH, value=homepageLocators.kids_option).click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.kids_text))
        )
        assert "MYNTRA FOR KIDS" in homepage.get_element_text(homepageLocators.kids_text), "we are not in kids page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_search_item(self):
        homepage = Homepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.search_field))
        )
        driver.find_element(by=By.XPATH, value=homepageLocators.search_field).send_keys("Jeans")
        driver.find_element(by=By.XPATH, value=homepageLocators.search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.category_verify))
        )
        assert "Jeans" in homepage.get_element_text(homepageLocators.category_verify), "We are not in jeans page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_select_item(self):
        homepage = Homepage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.search_field))
        )
        driver.find_element(by=By.XPATH, value=homepageLocators.search_field).send_keys("Jeans")
        driver.find_element(by=By.XPATH, value=homepageLocators.search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.category_verify))
        )
        assert "Jeans" in homepage.get_element_text(homepageLocators.category_verify), "We are not in jeans page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.first_item))
        )
        driver.find_element(by=By.XPATH, value=homepageLocators.first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, homepageLocators.item_verify))
        )
        assert "Jeans" in homepage.get_element_text(homepageLocators.item_verify), "jeans selection is wrong"
        driver.quit()
