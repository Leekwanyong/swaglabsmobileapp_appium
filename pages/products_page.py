from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

NATIVE_APP = "NATIVE_APP"

class ProductsPage(BasePage):
    product_items = {
        NATIVE_APP: (
            AppiumBy.ACCESSIBILITY_ID,
            "test-PRODUCTS"
        )
    }

    first_product = {
        NATIVE_APP: (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("test-Item").instance(0)'
        )
    }

    first_product_add_to_cart = {
        NATIVE_APP: (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("test-ADD TO CART").instance(0)'
        )
    }

    cart_badge = {
        NATIVE_APP: (
            AppiumBy.ACCESSIBILITY_ID,
            "test-Cart"
        )
    }

    def get_product_count(self):
        elements = self.find_elements(self.product_items)
        return len(elements)

    def is_products_loaded(self):
        return self.is_element_present(self.product_items)

    def click_first_product(self):
        self.click(self.first_product)

    def add_first_product_to_cart(self):
        self.click(self.first_product_add_to_cart)

    def open_cart(self):
        self.click(self.cart_badge)