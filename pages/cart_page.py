from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

NATIVE_APP = "NATIVE_APP"
class CartPage(BasePage):
    cart_item = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Item")
    }

    cart_amount = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Amount")
    }

    cart_description = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Description")
    }

    cart_price = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Price")
    }

    cart_remove_button = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")
    }

    cart_checkout = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
    }

    def get_item_count(self):
        element = self.find_elements(self.cart_item)
        return len(element)

    def has_items(self):
        return self.is_element_present(self.cart_item)

    def is_price_visible(self):
        return self.is_visible(self.cart_price)

    def is_description_visible(self):
        return self.is_visible(self.cart_description)

    def is_amount_visible(self):
        return self.is_visible(self.cart_amount)

    def remove_first_item(self):
        return self.click(self.cart_remove_button)

    def click_checkout(self):
        return self.click(self.cart_checkout)
