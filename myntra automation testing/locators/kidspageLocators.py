"""
Locators related to items page
"""


items_selection = "//li[@class='product-base']"
kids_shirts = "//a[normalize-space()='Shirts']"
women_button_1 = "//a[contains(text(),'Women')]"
women_text = "//strong[contains(text(),'ONLINE SHOPPING FOR WOMEN')]"
pincode = "//input[@type='tel']"
check_pincode = "//button[@type='submit']"
check_pincode_text = "//li[@class='pincode-serviceabilityItem'][position()=1]"
average_rating = "//div[@class='index-flexRow index-averageRating']"
rating_text = "//div[@id='headingContainer']"
verified_users = "//div[@class='index-countDesc']"
similar_products = "//div[@class='similar-container']//li[@class='product-list-gist'][position()=1]"
similar_products_text = "//h3[@class='similar-heading']"
price = "//span[@class='pdp-price']"
price_text = "//span[@class='pdp-vatInfo']"
