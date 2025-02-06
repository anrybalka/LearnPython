"""
2025 (C) anrybalka
"""
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://film-like.com/tag/1614-trevognie-filmi"


# def get_total_pages(browser):
#     browser.get(URL + "?page=1")
#     # Находим стрелку вправо не заблокированную
    


def returnNextPage(browser, startPageNum):
    """
    Проверяет, можно ли перейти на следующую страницу.
    Возвращает номер следующей страницы, если кнопка "Next" активна.
    """
    isNextExist = False
    isNextActive = False

    # Переход на страницу с номером startPageNum
    browser.get(URL + "?page=" + str(startPageNum))

    try:
        # Поиск кнопки "Next"
        nextButton = browser.find_element(By.CSS_SELECTOR, "div.list-view div.text-center ul.pagination li.next")
        isNextExist = True

        # Проверка, активна ли кнопка "Next"
        try:
            nextButtonDisabled = browser.find_element(By.CSS_SELECTOR, "div.list-view div.text-center ul.pagination li.next.disabled")
            isNextActive = False  # Кнопка неактивна
        except:
            isNextActive = True  # Кнопка активна
    except:
        isNextExist = False  # Кнопка "Next" не найдена

    # Возвращаем номер следующей страницы, если кнопка активна
    if isNextActive:
        return startPageNum + 1
    else:
        return startPageNum

def test_site2(browser):
    """
    Тест, который проверяет каждую страницу.
    """
    startPageNum = 1  # Начинаем с первой страницы

    while True:
        # Переход на страницу и проверка
        browser.get(URL + "?page=" + str(startPageNum))
        title = browser.title
        print("\n ----"+title)
        films = browser.find_elements(By.CSS_SELECTOR, ".name a")
        
        for film in films:
            print(film.text)

        # Пример проверки (замените на вашу логику)
        assert True, f"Ошибка для страницы {title}"

        # Проверяем, можно ли перейти на следующую страницу
        next_page = returnNextPage(browser, startPageNum)
        if next_page == startPageNum:
            break  # Если следующая страница недоступна, завершаем цикл

        startPageNum = next_page  # Переходим на следующую страницу
