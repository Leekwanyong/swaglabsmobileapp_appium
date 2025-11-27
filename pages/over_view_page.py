from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

NATIVE_APP = "NATIVE_APP"

class OverviewPage(BasePage):
    overview_title = {
        NATIVE_APP: (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("CHECKOUT: OVERVIEW")'
        )
    }

    product_items = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-Item")
    }

    finish_button = {
        NATIVE_APP: (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")
    }

    def is_loaded(self):
        """Overview 페이지 로딩"""
        return self.is_element_present(self.overview_title)

    def has_products(self):
        """상품 목록 있는지"""
        return self.is_element_present(self.product_items)

    def click_finish(self):
        """Finish 버튼 클릭"""
        self.scroll_to_element(self.finish_button)
        self.click(self.finish_button)