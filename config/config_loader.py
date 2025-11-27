import configparser
import json
import os
from json import JSONDecodeError

from appium import webdriver
from appium.options.android import UiAutomator2Options

SERVER_URL = "http://127.0.0.1:4723"
LOCAL_ENV = 'config/local.env.ini'
CPAS_JSON = 'config/capabilities.json'

# [LOCAL] ini 파일이 있는지 확인
def load_env():
    env = configparser.ConfigParser()
    path = os.path.exists(LOCAL_ENV)

    if not path:
        raise FileNotFoundError(f"{LOCAL_ENV} env 파일이 없음")
    env.read(LOCAL_ENV)
    if "LOCAL" not in env:
        raise KeyError("[LOCAL]이 없음")
    return env["LOCAL"]

# json 파일을 가져오기
def load_json():
    path = os.path.exists(CPAS_JSON)
    if not path:
        raise FileNotFoundError("json 파일이 없음")
    try:
        with open(CPAS_JSON, "r") as json_file:
            return json.load(json_file)
    except JSONDecodeError:
        raise ValueError("JSON 구조가 잘못됨")

def build_capabilities(json_path, env_data, install_app):
    caps = json_path.copy()

    print(f"DEBUG - env_data: {env_data}")
    print(f"DEBUG - install_app: {install_app}")

    # udid가 있으면 적용
    udid = env_data.get("udid")
    if udid:
        caps["udid"] = udid.strip('"')

    # apk 있으면 app capability override
    apk_path = env_data.get("apk")
    print(f"DEBUG - apk_path: {apk_path}")

    if install_app and apk_path:
        caps["app"] = apk_path.strip('"')

    print(f"DEBUG - final caps: {caps}")
    return caps

def create_driver(env, install_app, udid):
    ini = load_env()
    json_caps = load_json()

    if env:
        ini["env"] = env
    if udid:
        ini["udid"] = udid

    caps = build_capabilities(json_caps, ini, install_app)
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(SERVER_URL, options=options)
    driver.implicitly_wait(10)
    return driver



