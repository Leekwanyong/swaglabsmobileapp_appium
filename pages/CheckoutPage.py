from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

NATIVE_APP = "NATIVE_APP"
class CheckoutPage(BasePage):
    page_title = {
        NATIVE_APP: (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("CHECKOUT: INFORMATION")'
        )
    }

    first_name_input = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    }

    last_name_input = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    }

    zip_code_input = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    }

    continue_button = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")  # 확인 필요!
    }

    error_messages = {
        "first_name_required": {
            NATIVE_APP: (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("First Name is required")')
        },
        "last_name_required": {
            NATIVE_APP: (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Last Name is required")')
        },
        "zip_code_required": {
            NATIVE_APP: (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Postal Code is required")')
        }
    }

    def is_loaded(self):
        """결제 페이지 로딩됐는지"""
        return self.is_element_present(self.page_title)

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.send_keys(self.first_name_input, first_name)
        self.send_keys(self.last_name_input, last_name)
        self.send_keys(self.zip_code_input, zip_code)

    def click_continue(self):
        self.click(self.continue_button)

    def is_specific_error_visible(self, error_type):
        return self.is_visible(self.error_messages[error_type][NATIVE_APP])
