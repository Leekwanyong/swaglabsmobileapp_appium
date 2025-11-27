import pytest

from pages.CheckoutPage import CheckoutPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.regression
def test_empty_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_products_page_visible(), "로그인 실패: 상품 페이지가 보이지 않음"

    product_page = ProductsPage(driver)
    product_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 0, "장바구니가 비어있지 않음"

@pytest.mark.smoke
@pytest.mark.regression
def test_add_to_cart(driver):
    """상품 장바구니 담기"""
    # 1. 로그인
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_products_page_visible(), "로그인 실패: 상품 페이지가 보이지 않음"
    # 2. 상품 담기 (추가!)
    product_page = ProductsPage(driver)
    product_page.add_first_product_to_cart()
    # 3. 장바구니 열기
    product_page.open_cart()
    # 4. 검증 (수정!)
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1, "장바구니가 비어있음"

@pytest.mark.regression
def test_remove_from_cart(driver):
    """상품 장바구니 삭제"""
    # 1. 로그인
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_products_page_visible(), "로그인 실패: 상품 페이지가 보이지 않음"
    # 2. 상품 담기
    product_page = ProductsPage(driver)
    product_page.add_first_product_to_cart()
    # 3. 장바구니 열기
    product_page.open_cart()
    # 4. 검증
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1, "장바구니가 비어있음"
    #5 장바구니 삭제
    cart_page.remove_first_item()
    #6 삭제가 되었는지 확인
    assert cart_page.get_item_count() == 0, "장바구니가 비어있지 않음"

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout(driver):
    """상품 장바구니 담고 결제 페이지 진입"""
    # 1. 로그인
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_products_page_visible(), "로그인 실패: 상품 페이지가 보이지 않음"
    # 2. 상품 담기
    product_page = ProductsPage(driver)
    product_page.add_first_product_to_cart()
    # 3. 장바구니 열기
    product_page.open_cart()
    # 4. 검증
    cart_page = CartPage(driver)
    assert cart_page.get_item_count() == 1, "장바구니가 비어있음"
    # 5. 체크아웃 클릭
    cart_page.click_checkout()
    # 6. 결제 페이지 확인
    checkout_page = CheckoutPage(driver)
    assert checkout_page.is_loaded(), "결제 페이지로 이동 실패"
