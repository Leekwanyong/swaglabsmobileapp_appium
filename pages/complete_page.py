
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

NATIVE_APP = "NATIVE_APP"

class CompletePage(BasePage):
    complete_message = {
        NATIVE_APP: (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("THANK YOU FOR YOU ORDER")'
        )
    }

    def is_complete(self):
        """주문 완료 확인"""
        return self.is_element_present(self.complete_message)