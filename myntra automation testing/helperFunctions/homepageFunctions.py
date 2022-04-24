from helperFunctions.conftest import *
from locators import homepageLocators
"""Helper Functions related to home page"""


class Homepage:
    def get_element_text(self, element: str) -> str:
        """
            It is getting text of any element
            :param element: xpath of element which has text
            :return: text
        """
        text = driver.find_element(by=By.XPATH,value=element).text
        return text

    def click_profile_button(self) -> None:
        """
        for clicking profile button
        :return: None
        """
        driver.find_element(by=By.XPATH,value=homepageLocators.profile_button).click()

    def click_contact_button(self) -> None:
        """
        for clicking contact button
        :return: None
        """

        driver.find_element(by=By.XPATH, value=homepageLocators.contact_us).click()

    def switching_windows(self) -> None:
        """
            It is used to switch windows
            :return:None
        """
        ids = driver.window_handles
        driver.switch_to.window(ids[1])
        driver.close()
        driver.switch_to.window(ids[0])



