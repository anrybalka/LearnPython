"""
Fixture
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    """
    Main fixture
    """
    # оптимизация запуска Chrome
    chrome_options = Options()
    prefs = {
    "profile.managed_default_content_settings.images": 2,  # Отключаем загрузку изображений
    "profile.default_content_setting_values.javascript": 2,  # Опционально: отключаем JavaScript
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    # установить свежий драйвер прослойку между кодом и браузером
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    browser.quit()
