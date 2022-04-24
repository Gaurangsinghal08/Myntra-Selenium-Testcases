
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from helperFunctions.kidsPageFunctions import *
"""
Author: Gaurang Singhal
Date Created: 25/03/2022
Date Modified: 06/04/2022
Test Case related to kids page
"""


class TestKidsPage:
    @pytest.mark.usefixtures("helper_function")
    def test_user_is_on_kids_page(self):
        kidspage = Kidspage()
        driver.save_screenshot("a.png")
        kidspage.go_to_kids_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_text))
        )
        assert "MYNTRA FOR KIDS" in kidspage.get_element_text(kids_text), "we are not in kids page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_count_list_items(self):
        kidspage = Kidspage()
        kidspage.go_to_kids_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_text))
        )
        assert "MYNTRA FOR KIDS" in kidspage.get_element_text(kids_text), "we are not in kids page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("kids tshirt")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Tshirts" in kidspage.get_element_text(category_verify), "We are kids tshirt page"
        list_of_items = driver.find_elements(by=By.XPATH, value=items_selection)
        print("There are {} items in this category".format(len(list_of_items)))
        assert 50 == len(list_of_items)

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_kids_shirts(self):
        kidspage = Kidspage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_option))
        )
        kids = driver.find_element(by=By.XPATH, value=kids_option)
        action = ActionChains(driver)
        action.move_to_element(kids).perform()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_shirts))
        )
        driver.find_element(by=By.XPATH, value=kids_shirts).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Kids" in kidspage.get_element_text(category_verify), "we are not kids shirts page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_switch_into_women_page(self):
        kidspage = Kidspage()
        kidspage.go_to_kids_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_text))
        )
        assert "MYNTRA FOR KIDS" in kidspage.get_element_text(kids_text), "we are not in kids page"
        driver.find_element(by=By.XPATH, value=women_button_1).click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert "ONLINE SHOPPING FOR WOMEN" in kidspage.get_element_text(women_text)

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_select_particular_item(self):
        kidspage = Kidspage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Shirts kids")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Shirts" in kidspage.get_element_text(category_verify), "We are not in kids shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Shirt" in kidspage.get_element_text(item_verify), "shirt selection is wrong"
        kidspage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_check_product_is_available_in_his_location(self):
        kidspage = Kidspage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Shirts kids")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Shirts" in kidspage.get_element_text(category_verify), "We are not in kids shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Shirt" in kidspage.get_element_text(item_verify), "we are not in shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pincode))
        )
        driver.find_element(by=By.XPATH, value=pincode).send_keys("302020")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, check_pincode))
        )
        driver.find_element(by=By.XPATH, value=check_pincode).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, check_pincode_text))
        )
        assert "Get it by" in kidspage.get_element_text(check_pincode_text), "item not available"
        kidspage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_check_product_rating(self):
        kidspage = Kidspage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Shirts kids")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Shirts" in kidspage.get_element_text(category_verify), "We are not in kids shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Shirt" in kidspage.get_element_text(item_verify), "shirt selection is wrong"
        print("average rating of the product is {}".format(kidspage.get_element_text(average_rating)))
        assert "RATINGS" in kidspage.get_element_text(rating_text), "rating is missing"
        kidspage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_no_of_verified_buyers(self):
        kidspage = Kidspage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Shirts kids")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Shirts" in kidspage.get_element_text(category_verify), "We are not in kids shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Shirt" in kidspage.get_element_text(item_verify), "shirt selection is wrong"
        no_of_users = (kidspage.get_element_text(verified_users))
        k = no_of_users.split()
        print("Number of verified users are {}".format(k[0]))
        assert "Verified Buyers" in no_of_users, "Verified Buyers missing"
        kidspage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_price_of_a_item(self):
        kidspage = Kidspage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Shirts kids")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Shirts" in kidspage.get_element_text(category_verify), "We are not in kids shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Shirt" in kidspage.get_element_text(item_verify), "shirt selection is wrong"
        price_of_product = (kidspage.get_element_text(price))
        print("Price of item is {}".format(price_of_product))
        assert "inclusive of all taxes" in kidspage.get_element_text(price_text), "price of item missing"
        kidspage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_select_similar_products(self):
        kidspage = Kidspage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Shirts kids")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Shirts" in kidspage.get_element_text(category_verify), "We are not in kids shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Shirt" in kidspage.get_element_text(item_verify), "shirt selection is wrong"
        driver.execute_script("window.scrollTo(0, 2500);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, similar_products))
        )
        driver.find_element(by=By.XPATH, value=similar_products).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, similar_products_text))
        )
        assert "SIMILAR PRODUCTS" in kidspage.get_element_text(similar_products_text), "similar products missing"
        driver.quit()
