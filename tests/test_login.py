import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password, expected_result, error_type", [
    # 성공 케이스
    ("standard_user", "secret_sauce", "success", None),
    # 실패 케이스 - 잘못된 credential
    ("standard_user", "secret_sauce1", "fail", "invalid_credentials"),
    # 실패 케이스 - 아이디 미입력
    ("", "secret_sauce", "fail", "username_required"),
    # 실패 케이스 - 비밀번호 미입력
    ("standard_user", "", "fail", "password_required"),
    # 실패 케이스 - 둘다 미입력
    ("", "", "fail", "username_required"),
    # 뒤 공백
    ("standard_user ", "secret_sauce", "fail", "invalid_credentials"),
    # 앞 공백
    (" standard_user", "secret_sauce", "fail", "invalid_credentials"),
])
def test_login_scenarios(driver, username, password, expected_result, error_type):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected_result == "success":
        assert login_page.is_products_page_visible(), "로그인 실패: 상품 페이지가 보이지 않음"
    else:
        assert login_page.is_specific_error_visible(error_type), f"예상 에러 '{error_type}'가 표시되지 않음"
