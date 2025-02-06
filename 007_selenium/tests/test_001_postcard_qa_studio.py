"""
2025 (C) anrybalka
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://film-like.com/spisok/713-filmi-dlya-podnyatiya-motivatsii"

def test_button(browser):
    """
    TEST-1. button test
    """
    browser.get(URL)
    button = browser.find_element(by=By.ID, value="send")
    assert button.text == "Отправить", f"Unexpected text on button {button.text}"

def test_class(browser):
    """
    TEST-2. class test
    """
    browser.get(URL)
    
    email_lable = browser.find_element(by=By.CSS_SELECTOR, value="div.email h2")
    email_lable_class = email_lable.get_attribute("class")

    assert email_lable_class == "requered", f"Unexpected text {button.text}"

    button = browser.find_element(by=By.ID, value="send")
    button.click()

    email_lable = browser.find_element(by=By.CSS_SELECTOR, value="div.email h2")
    email_lable_class = email_lable.get_attribute("class")

    assert email_lable_class == "requered error", f"Unexpected text {button.text}"


CASE = [0, 1]
@pytest.mark.parametrize('case', CASE)
def test_send_postcard(browser, case):
    """
    TEST-3. test_send_postcard
    """
    browser.get(URL)

    email = browser.find_element(by=By.ID, value="email")
    email.click()
    email.send_keys("tocinid643@shouxs.com")

    textarea = browser.find_element(by=By.ID, value="textarea")
    textarea.click()
    textarea.send_keys("TEST-3. test_send_postcard")

    images = browser.find_elements(by=By.CLASS_NAME, value="photo-input__photo")

    image1 = images[case]
    image1.click()

    button = browser.find_element(by=By.ID, value="send")
    button.click()

    ok_message = browser.find_element(by=By.CSS_SELECTOR, value="#modal div h3")
    ok_message_text = ok_message.text

    assert ok_message_text == "Открытка успешно отправлена!", "Ошибка с отправкой открытки"
