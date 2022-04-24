from helperFunctions.conftest import *
from locators.ProfilePageLocators import *
"""Helper Functions related to profilepage"""


class Profilepage:
    def go_to_profile_page(self) -> None:
        """
            used to go to profile page from homepage
            :return: None
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, profile_button))
        )
        driver.find_element(by=By.XPATH, value=profile_button).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, edit_profile_button))
        )
        driver.find_element(by=By.XPATH, value=edit_profile_button).click()

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
