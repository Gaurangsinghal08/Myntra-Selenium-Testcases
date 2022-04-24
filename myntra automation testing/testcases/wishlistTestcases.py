from helperFunctions.wishlistFunctions import *
from selenium.webdriver import Keys
from locators.wishlistPageLocators import *
"""
Author: Gaurang Singhal
Date Created: 25/03/2022
Date Modified: 06/04/2022
Test Case related to wishlist page
"""


@pytest.mark.usefixtures("helper_function", "login_and_logout")
class TestWishlistPage:

    def test_wishlist_page_is_visible(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_button))
        )
        wishlist = WishlistPage()
        wishlist.go_to_wishlist_page()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_text))
        )
        assert wishlist.get_element_text(wishlist_text) == "My Wishlist"

    def test_user_can_see_count_of_wishlist_items(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_button))
        )
        wishlist = WishlistPage()
        wishlist.go_to_wishlist_page()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_text))
        )
        assert wishlist.get_element_text(wishlist_text) == "My Wishlist"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_field))
        )

        items_wishlist = driver.find_elements(by=By.XPATH, value=items_in_wishlist)
        i = len(items_wishlist)
        assert str(i) in wishlist.get_element_text(count_text), "count is wrong"

    # def test_user_can_go_to_wishlist_page_from_bag_page(self):
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, cart_button))
    #     )
    #     cart_button_field = driver.find_element(by=By.XPATH, value=cart_button)
    #     assert cart_button_field.is_displayed(), "cart button missing"
    #     cart_button_field.click()
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, add_items_from_wishlist))
    #     )
    #     add_items_from_wishlist_field = driver.find_element(by=By.XPATH, value=add_items_from_wishlist)
    #     assert add_items_from_wishlist_field.is_displayed(), "wishlist is missing"
    #     add_items_from_wishlist.click()

    def test_user_can_delete_items_from_wishlist(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_button))
        )
        wishlist = WishlistPage()
        wishlist.go_to_wishlist_page()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, remove_icon))
        )
        count_of_wishlist_items = driver.find_elements(by=By.XPATH, value=count_items)

        remove_first_item = driver.find_element(by=By.XPATH, value=remove_icon)
        remove_first_item.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, count_items))
        )
        updated_count = driver.find_elements(by=By.XPATH, value=count_items)
        assert (len(count_of_wishlist_items)) == (len(updated_count)), "removal of item is failed"

    @pytest.mark.usefixtures("helper_function", "login_and_logout")
    def test_user_can_see_first_item_from_wishlist(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_button))
        )
        wishlist = WishlistPage()
        wishlist.go_to_wishlist_page()
        assert "wishlist" in driver.current_url, "we are not in wishlist page"
        item_of_wishlist = driver.find_element(by=By.XPATH, value=first_item_in_wishlist)
        item_of_wishlist.click()
        wishlist.switching_windows()

    def test_user_can_add_items_to_wishlist(self):
        wishlist = WishlistPage()
        search_field_text = driver.find_element(by=By.XPATH, value=search_field)
        assert search_field_text.is_displayed(), "search field is missing"
        search_field_text.send_keys("jeans men")
        driver.find_element(by=By.XPATH, value=search_field).send_keys(Keys.ENTER)
        assert "Jeans" in wishlist.get_element_text(category_verify), "search result is wrong"
        select_product = driver.find_element(by=By.XPATH, value=first_item)
        select_product.click()
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        wishlist_item = driver.find_element(by=By.XPATH, value=wishlist_particular_item)
        wishlist_item.click()

    @pytest.mark.usefixtures("helper_function", "login_and_logout")
    def test_user_can_select_wishlist_items(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_button))
        )
        wishlist = WishlistPage()
        wishlist.go_to_wishlist_page()
        assert "wishlist" in driver.current_url, "we are not in wishlist page"
        item_of_wishlist = driver.find_element(by=By.XPATH, value=first_item_in_wishlist)
        item_of_wishlist.click()
        wishlist.switching_windows()

    def test_user_can_add_to_cart_wishlist_items(self):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, wishlist_button))
        )
        wishlist = WishlistPage()
        wishlist.go_to_wishlist_page()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, move_to_bag_icon))
        )
        driver.find_element(by=By.XPATH, value=move_to_bag_icon).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_size))
        )
        driver.find_element(by=By.XPATH, value=first_size).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, add_to_cart))
        )
        driver.find_element(by=By.XPATH, value=add_to_cart).click()

        driver.quit()
