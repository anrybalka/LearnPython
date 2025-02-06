"""
2025 (C) anrybalka
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_smoke(browser):
    """
    TEST-ID. Smoke test
    """
    browser.get("https://postcard.qa.studio/")
    button = browser.find_element(by=By.ID, value="send")
    assert button.text == "Отправить", f"Unexpected text on button {button.text}"
