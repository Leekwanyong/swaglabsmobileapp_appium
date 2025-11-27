from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

NATIVE_APP = "NATIVE_APP"

class LoginPage(BasePage):
    username_input = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    }
    password_input = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    }
    login_button = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    }

    product_item = {
        NATIVE_APP: (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("test-Item").instance(0)'
        )
    }

    error_messages = {
        "invalid_credentials": {
            NATIVE_APP: (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Username and password do not match any user in this service.")')
        },
        "username_required": {
            NATIVE_APP: (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Username is required")')
        },
        "password_required": {
            NATIVE_APP: (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Password is required")')
        }
    }

    def login(self, username, password):
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)

    def is_products_page_visible(self):
        return self.is_element_present(self.product_item, timeout=5)

    def is_specific_error_visible(self, error_type):
        return self.is_visible(self.error_messages[error_type][NATIVE_APP])
