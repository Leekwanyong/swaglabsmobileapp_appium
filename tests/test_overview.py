import pytest

from pages.CheckoutPage import CheckoutPage
from pages.cart_page import CartPage
from pages.complete_page import CompletePage
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
    checkout_page.click_continue()

    # 6. Overview 페이지 확인
    overview_page = OverviewPage(driver)
    assert overview_page.is_loaded(), "주문 확인 페이지로 이동 실패"
    assert overview_page.has_products(), "상품 정보가 없음"

    # 7. Finish 클릭
    overview_page.click_finish()
    #8 완료확인
    complete_page = CompletePage(driver)
    assert complete_page.is_complete(), "주문 완료 메시지가 표시되지 않음"

