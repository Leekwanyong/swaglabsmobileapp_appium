from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 15


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 하이브리드 앱 둘다 지원
    def auto_switch_context(self):
        current = self.driver.current_context

        if current and "WEBVIEW" in current:
            return "WEBVIEW"

        if current and "NATIVE_APP" in current:
            return "NATIVE_APP"

        contexts = self.driver.contexts
        for ctx in contexts:
            if "WEBVIEW" in ctx:
                self.driver.switch_to.context(ctx)
                return "WEBVIEW"

        if "NATIVE_APP" in contexts:
            self.driver.switch_to.context("NATIVE_APP")
            return "NATIVE_APP"

        return None

    def _get_appropriate_locator(self, locators):
        current_context = self.auto_switch_context()

        locators_to_use = locators.get(current_context)

        if locators_to_use is None:
            if current_context == "WEBVIEW":
                locators_to_use = locators.get("NATIVE_APP")
            elif current_context == "NATIVE_APP":
                locators_to_use = locators.get("WEBVIEW")

            if locators_to_use is None:
                raise ValueError(
                    f"'{current_context}' 및 fallback에도 locator가 없음"
                    f"제공된 keys: {list(locators.keys())}"
                )

        return locators_to_use

    # DOM에 존재하고 화면에 표시 되는가?
    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"{locator} 시간 초과")

    def is_clickable(self, locator):
        try:
            element = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"{locator} 시간 초과")

    def is_element_present(self, locator, timeout=DEFAULT_TIMEOUT):
        locator = self._get_appropriate_locator(locator)
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # 여러 요소 찾기
    def find_elements(self, locators, timeout=DEFAULT_TIMEOUT):
        locator = self._get_appropriate_locator(locators)

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []

    def click(self, locators):
        locator = self._get_appropriate_locator(locators)

        if locator:
            element = self.is_clickable(locator)
            element.click()

    def send_keys(self, locators, text):
        locator = self._get_appropriate_locator(locators)

        if locator:
            element = self.is_clickable(locator)
            element.click()
            element.clear()
            element.send_keys(text)

    def swipe(self, direction, duration=800):
        devices_size  = self.driver.get_window_size()
        screen_size = devices_size["width"]
        screen_height = devices_size["height"]

        center_x = screen_size / 2
        center_y = screen_height / 2

        swipe_actions = {
            "up" : (center_x, screen_height * 0.8, center_x, screen_height * 0.2),
            "down" : (center_x, screen_height * 0.2, center_x, screen_height * 0.8),
            "left" : (screen_size * 0.8, center_y, screen_size * 0.2, center_y),
            "right" : (screen_size * 0.2, center_y, screen_size * 0.8, center_y),
        }

        if direction not in swipe_actions:
            raise ValueError("속 하는 값이 없음")

        start_x, start_y, end_x, end_y = swipe_actions[direction]
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def scroll_to_element(self, locators, direction="up", max_scroll=10):
        locator = self._get_appropriate_locator(locators)

        for attempt in range(max_scroll):
            try:
                element = self.is_visible(locator, 2)
                return element
            except TimeoutException:
                if attempt == max_scroll - 1:
                    raise TimeoutException(f"마지막 시도를 했지만 찾지 못함 '{locator}'")
                self.swipe(direction)
        return None

    def press_back(self):
        self.driver.back()

    def get_text(self, locators):
        locator = self._get_appropriate_locator(locators)

        element = self.is_visible(locator)

        return element.text