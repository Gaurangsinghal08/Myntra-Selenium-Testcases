import time
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from helperFunctions.womenPageFunction import *
"""
Author: Gaurang Singhal
Date Created: 25/03/2022
Date Modified: 06/04/2022
Test Case related to women page
"""


class TestWomenPage:
    @pytest.mark.usefixtures("helper_function")
    def test_user_is_on_women_page(self):
        womenpage = Womenpage()
        womenpage.go_to_women_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert "ONLINE SHOPPING FOR WOMEN" in womenpage.get_element_text(women_text)

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_count_list_items(self):
        womenpage = Womenpage()
        womenpage.go_to_women_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert "ONLINE SHOPPING FOR WOMEN" in womenpage.get_element_text(women_text)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Women Suits")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Women Suits" in womenpage.get_element_text(category_verify), "We are not in men suits page"
        list_of_items = driver.find_elements(by=By.XPATH, value=items_selection)
        print("There are {} items in this category".format(len(list_of_items)))
        assert 50 == len(list_of_items)

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_women_ethnic_wear(self):
        womenpage = Womenpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, women_button))
        )
        women = driver.find_element(by=By.XPATH, value=women_button)
        action = ActionChains(driver)
        action.move_to_element(women).perform()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ethnic_wear))
        )
        driver.find_element(by=By.XPATH, value=ethnic_wear).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Ethnic Wear" in womenpage.get_element_text(category_verify), "we are not in Ethnic Wear page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_switch_into_kids_page(self):
        womenpage = Womenpage()
        womenpage.go_to_women_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert "ONLINE SHOPPING FOR WOMEN" in womenpage.get_element_text(women_text)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_option))
        )
        driver.find_element(by=By.XPATH, value=kids_option).click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_text))
        )
        assert "MYNTRA FOR KIDS" in womenpage.get_element_text(kids_text), "we are not in kids page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_select_particular_item(self):
        womenpage = Womenpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("ethnic wear women")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Ethnic Wear" in womenpage.get_element_text(category_verify), "We are not in ethnic wear page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Ethnic" in womenpage.get_element_text(item_verify), "suit selection is wrong"
        womenpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_check_product_is_available_in_his_location(self):
        womenpage = Womenpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Women Tops")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Tops" in womenpage.get_element_text(category_verify), "We are not in women tops page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Top" in womenpage.get_element_text(item_verify), "we are not in tops page"
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
        assert "Get it by" in womenpage.get_element_text(check_pincode_text), "item not available"
        womenpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_check_product_rating(self):
        womenpage = Womenpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Women Tops")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Tops" in womenpage.get_element_text(category_verify), "We are not in women tops page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Top" in womenpage.get_element_text(item_verify), "tops selection is wrong"
        print("average rating of the product is {}".format(womenpage.get_element_text(average_rating)))
        assert "RATINGS" in womenpage.get_element_text(rating_text), "rating is missing"
        womenpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_no_of_verified_buyers(self):
        womenpage = Womenpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Women Tops")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Tops" in womenpage.get_element_text(category_verify), "We are not in women tops page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Top" in womenpage.get_element_text(item_verify), "tops selection is wrong"
        no_of_users = (womenpage.get_element_text(verified_users))
        k = no_of_users.split()
        print("Number of verified users are {}".format(k[0]))
        assert "Verified Buyers" in no_of_users, "Verified Buyers missing"
        womenpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_price_of_a_item(self):
        womenpage = Womenpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Women Tops")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Tops" in womenpage.get_element_text(category_verify), "We are not in women tops page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Top" in womenpage.get_element_text(item_verify), "tops selection is wrong"
        price_of_product = (womenpage.get_element_text(price))
        print("Price of item is {}".format(price_of_product))
        assert "inclusive of all taxes" in womenpage.get_element_text(price_text), "price of item missing"
        womenpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_select_similar_products(self):
        womenpage = Womenpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Women Tops")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, category_verify))
        )
        assert "Tops" in womenpage.get_element_text(category_verify), "We are not in women tops page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Top" in womenpage.get_element_text(item_verify), "tops selection is wrong"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, similar_products))
        )
        time.sleep(1)
        driver.find_element(by=By.XPATH, value=similar_products).click()
        assert "SIMILAR PRODUCTS" in womenpage.get_element_text(similar_products_text), "similar products missing"
        driver.quit()
