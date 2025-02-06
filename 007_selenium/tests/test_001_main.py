"""
2025 (C) anrybalka
"""
from selenium import webdriver

def test_smoke():
    """
    TEST-ID. Smoke test
    """
    driver = webdriver.Chrome()
    driver.get("http://selenium.dev")
    driver.quit()

    assert True, ""
