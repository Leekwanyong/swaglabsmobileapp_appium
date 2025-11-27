# Shopping Android Appium Test Automation

Appium을 사용한 Android 쇼핑 앱 (Sauce Labs Demo App) 자동화 테스트 프로젝트입니다.

## 프로젝트 구조

```
shopping_android_appium/
├── config/                     # 설정 파일
│   ├── config_loader.py       # Appium 드라이버 생성 및 설정 로더
│   ├── capabilities.json      # Appium capabilities 설정
│   └── local.env.ini          # 로컬 환경 설정 (UDID, APK 경로 등)
├── pages/                      # Page Object Model 클래스
│   ├── base_page.py           # 공통 메서드 (wait, click, swipe 등)
│   ├── login_page.py          # 로그인 페이지
│   ├── products_page.py       # 상품 목록 페이지
│   ├── cart_page.py           # 장바구니 페이지
│   ├── CheckoutPage.py        # 결제 정보 입력 페이지
│   ├── over_view_page.py      # 주문 확인 페이지
│   └── complete_page.py       # 주문 완료 페이지
├── tests/                      # 테스트 케이스
│   ├── test_login.py          # 로그인 테스트
│   ├── test_cart.py           # 장바구니 테스트
│   ├── test_checkout.py       # 결제 테스트
│   └── test_overview.py       # 주문 완료 테스트
├── conftest.py                 # pytest fixture 설정
├── pytest.ini                  # pytest 설정 및 마커
└── README.md
```

## 주요 기능

- Page Object Model (POM) 디자인 패턴 적용
- pytest 기반 테스트 프레임워크
- Parametrize를 활용한 데이터 주도 테스트
- Hybrid 앱 (Native/WebView) 지원
- 자동 context switching 기능
- Smoke/Regression 테스트 마커 구분

## 사전 요구사항

### 1. 환경 설정

- Python 3.8 이상
- Node.js 및 npm
- Appium Server 2.x
- Android SDK
- 실제 Android 기기 또는 에뮬레이터

### 2. Appium 설치

```bash
npm install -g appium
appium driver install uiautomator2
```

### 3. Python 패키지 설치

```bash
pip install -r requirements.txt
```

주요 패키지:

- appium-python-client
- selenium
- pytest

## 설정 방법

### 1. config/local.env.ini 파일 생성

```ini
[LOCAL]
udid = your_device_udid
apk = path/to/your/app.apk
```

UDID 확인 방법:

```bash
adb devices
```

## 테스트 실행

### Appium Server 시작

```bash
appium
```

기본 포트: http://127.0.0.1:4723

### 전체 테스트 실행

```bash
pytest tests/
```

### 특정 테스트 파일 실행

```bash
pytest tests/test_login.py
```

### 마커별 실행

```bash
# Smoke 테스트만 실행
pytest -m smoke

# Regression 테스트만 실행
pytest -m regression
```

### 옵션과 함께 실행

```bash
# 로컬 환경에서 실행
pytest tests/ --env=local

# APK 설치하며 실행
pytest tests/ --env=local --install_app

# 특정 기기 UDID 지정
pytest tests/ --env=local --udid=your_device_udid
```

## 테스트 케이스

### test_login.py

- 정상 로그인
- 잘못된 credential
- 아이디/비밀번호 미입력
- 공백 포함 입력 검증

### test_cart.py

- 빈 장바구니 확인
- 장바구니에 상품 추가
- 장바구니에서 상품 삭제
- 결제 페이지 진입

### test_checkout.py

- 결제 정보 입력
- 필수 필드 검증

### test_overview.py

- 주문 확인
- 주문 완료 플로우

## Page Object 구조

### BasePage

모든 페이지 클래스의 기본 클래스로 공통 메서드 제공:

- `is_visible()`: 요소 표시 대기
- `is_clickable()`: 클릭 가능 대기
- `click()`: 요소 클릭
- `send_keys()`: 텍스트 입력
- `swipe()`: 스와이프 동작
- `scroll_to_element()`: 요소까지 스크롤
- `auto_switch_context()`: Native/WebView 자동 전환

## 주요 특징

### 1. Hybrid 앱 지원

- Native와 WebView context를 자동으로 감지하고 전환합니다.

### 2. Parametrize 테스트

- 다양한 시나리오를 효율적으로 테스트합니다.

### 3. 자동 앱 재시작

- 각 테스트 후 앱을 자동으로 재시작하여 깨끗한 상태를 유지합니다.

### 앱이 설치되지 않음

- `config/local.env.ini`에서 APK 경로 확인
- `--install_app` 옵션 사용

## 테스트 대상 앱

- 앱 이름: Sauce Labs Demo App
- Package: `com.swaglabsmobileapp`
- Activity: `com.swaglabsmobileapp.MainActivity`
- 다운로드: [Sauce Labs GitHub](https://github.com/saucelabs/sample-app-mobile)

## 참고 자료

- [Appium 공식 문서](https://appium.io/docs/en/latest/)
- [Pytest 문서](https://docs.pytest.org/)
- [Selenium Python 문서](https://selenium-python.readthedocs.io/)