import pytest

from pages.CheckoutPage import CheckoutPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.over_view_page import OverviewPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_success(driver):
    """정상 체크아웃 플로우"""
    # 1. 로그인
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_products_page_visible()
    # 2. 상품 담기
    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()
    # 3. 장바구니 확인
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1
    # 4. 체크아웃 클릭
    cart_page.click_checkout()
    # 5. 정보 입력
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("a", "b", "c")
    # 6. Continue 클릭
    checkout_page.click_continue()
    # 7. 오버뷰 이동 확인
    overview_page = OverviewPage(driver)
    assert overview_page.is_loaded(), "주문 상세정보 타이틀이 표시되지 않음"

@pytest.mark.regression
@pytest.mark.parametrize("first_name, last_name, zip_code, error_type", [
    ("", "Doe", "12345", "first_name_required"),
    ("John", "", "12345", "last_name_required"),
    ("John", "Doe", "", "zip_code_required"),
])
def test_checkout_validation(driver, first_name, last_name, zip_code, error_type):
    """체크아웃 유효성 검증"""
    # 1. 로그인
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_products_page_visible(), "상품이 없음"
    # 2. 상품 담기
    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()
    # 3. 장바구니
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1, "장바구니가 비어있음"
    # 4. 체크아웃 클릭
    cart_page.click_checkout()
    # 5. 빈 값 입력
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info(first_name, last_name, zip_code)
    # 6. Continue 클릭
    checkout_page.click_continue()
    # 7. 에러 메시지 확인
    assert checkout_page.is_specific_error_visible(error_type), f"에러 '{error_type}'가 표시되지 않음"
