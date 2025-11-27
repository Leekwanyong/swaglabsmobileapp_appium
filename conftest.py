import pytest

from config.config_loader import create_driver


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="로컬에서 실행")
    parser.addoption("--install_app", action="store_true", default=False, help="apk가 설치되어 있지 않으시")
    parser.addoption("--udid", action="store", default=None, help="핸드폰으로 테스트 시 UDID값은 필수")

@pytest.fixture(scope="session")
def driver(request):
    env = request.config.getoption("--env")
    install_app = request.config.getoption("--install_app")
    udid = request.config.getoption("--udid")
    driver = create_driver(env, install_app, udid)
    yield driver
    if driver:
        driver.quit()

@pytest.fixture(scope="function", autouse=True)
def reset_app(driver):
    yield
    driver.terminate_app("com.swaglabsmobileapp")
    driver.activate_app("com.swaglabsmobileapp")
