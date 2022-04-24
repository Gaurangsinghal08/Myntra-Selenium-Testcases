from locators.wishlistPageLocators import *
from helperFunctions.conftest import *
"""Helper Functions related to wishlist page"""


class WishlistPage:
    def go_to_wishlist_page(self) -> None:
        """
            used to go to wishlist page from homepage
            :return: None
        """
        driver.find_element(by=By.XPATH, value=wishlist_button).click()

    def get_element_text(self, element: str) -> str:
        """
            It is getting text of any element
            :param element: xpath of element which has text
            :return: text
        """
        text = driver.find_element(by=By.XPATH, value=element).text
        return text

    def switching_windows(self) -> None:
        """
            It is used to switch active window screen
            :return:None
        """
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        driver.close()
        driver.switch_to.window(ids[0])
