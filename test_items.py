import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    add_button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert add_button.is_displayed(), 'Кнопки "Добавить в корзину" нет на странице' 

