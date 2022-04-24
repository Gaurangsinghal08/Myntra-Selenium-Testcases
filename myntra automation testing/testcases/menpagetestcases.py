from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from helperFunctions.menPageFunctions import *
"""
Author: Gaurang Singhal
Date Created: 25/03/2022
Date Modified: 06/04/2022
Test Case related to men page
"""


class TestMenPage:
    @pytest.mark.usefixtures("helper_function")
    def test_user_is_on_men_page(self):
        menpage = Menpage()
        menpage.go_to_men_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert "ONLINE SHOPPING FOR MEN" in menpage.get_element_text(men_page_text)

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_count_list_items(self):
        menpage = Menpage()
        menpage.go_to_men_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert "ONLINE SHOPPING FOR MEN" in menpage.get_element_text(men_page_text)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Men Suits")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Men Suits" in menpage.get_element_text(catagory_verify), "We are not in men suits page"
        list_of_items = driver.find_elements(by=By.XPATH, value=items_selection)
        print("There are {} items in this category".format(len(list_of_items)))
        assert 50 == len(list_of_items), "count of items is not correct"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_men_formal_shirts(self):
        menpage = Menpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, men_button))
        )
        men = driver.find_element(by=By.XPATH, value=men_button)
        action = ActionChains(driver)
        action.move_to_element(men).perform()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, formal_shirts_option))
        )
        driver.find_element(by=By.XPATH, value=formal_shirts_option).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Formal Shirts" in menpage.get_element_text(catagory_verify), "we are not in formal shirts page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_switch_into_kids_page(self):
        menpage = Menpage()
        menpage.go_to_men_page()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        assert "ONLINE SHOPPING FOR MEN" in menpage.get_element_text(men_page_text)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_option))
        )
        driver.find_element(by=By.XPATH, value=kids_option).click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kids_text))
        )
        assert "MYNTRA FOR KIDS" in menpage.get_element_text(kids_text), "we are not in kids page"

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_select_particular_item(self):
        menpage = Menpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Men Suits")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Men Suits" in menpage.get_element_text(catagory_verify), "We are not in men suits page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Suit" in menpage.get_element_text(item_verify), "suit selection is wrong"
        menpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_check_product_is_available_in_his_location(self):
        menpage = Menpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Men Shirts")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Shirts" in menpage.get_element_text(catagory_verify), "We are not in men shirts page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Shirt" in menpage.get_element_text(item_verify), "we are not in shirts page"
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
        assert "Get it by" in menpage.get_element_text(check_pincode_text), "item not available"
        menpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_check_product_rating(self):
        menpage = Menpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Men Jeans")

        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Jeans" in menpage.get_element_text(catagory_verify), "We are not in men jeans page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Jeans" in menpage.get_element_text(item_verify), "jeans selection is wrong"
        print("average rating of the product is {}".format(menpage.get_element_text(average_rating)))
        assert "RATINGS" in menpage.get_element_text(rating_text), "rating is missing"
        menpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_see_no_of_verified_buyers(self):
        menpage = Menpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Men Jeans")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Jeans" in menpage.get_element_text(catagory_verify), "We are not in men jeans page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Jeans" in menpage.get_element_text(item_verify), "jeans selection is wrong"
        no_of_users = (menpage.get_element_text(verified_users))
        k = no_of_users.split()
        print("Number of verified users are {}".format(k[0]))
        assert "Verified Buyers" in no_of_users, "Verified Buyers missing"
        menpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_find_price_of_a_item(self):
        menpage = Menpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Men Jeans")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Jeans" in menpage.get_element_text(catagory_verify), "We are not in men jeans page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Jeans" in menpage.get_element_text(item_verify), "jeans selection is wrong"
        price_of_product = (menpage.get_element_text(price))
        print("Price of item is {}".format(price_of_product))
        assert "inclusive of all taxes" in menpage.get_element_text(price_text), "price of item missing"
        menpage.switching_windows()

    @pytest.mark.usefixtures("helper_function")
    def test_user_is_able_to_select_similar_products(self):
        menpage = Menpage()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )
        driver.find_element(by=By.XPATH, value=search_field).send_keys("Men Jeans")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, catagory_verify))
        )
        assert "Jeans" in menpage.get_element_text(catagory_verify), "We are not in men jeans page"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_item))
        )
        driver.find_element(by=By.XPATH, value=first_item).click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, item_verify))
        )
        assert "Jeans" in menpage.get_element_text(item_verify), "jeans selection is wrong"

        driver.execute_script("window.scrollTo(0, 2500);")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, similar_products))
        )
        driver.find_element(by=By.XPATH, value=similar_products).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, similar_products_text))
        )
        # assert "SIMILAR PRODUCTS" in menpage.get_element_text(similar_products_text), "similar products missing"
        driver.quit()
