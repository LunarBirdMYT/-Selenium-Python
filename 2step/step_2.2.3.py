# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

def calc(x, y):
    return int(x) + int(y)
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # находим элемент "х" и "y" на странице и преобразуем веб элемент в текст
    x_site = browser.find_element_by_css_selector('#num1').text
    y_site = browser.find_element_by_css_selector('#num2').text
    sum_out = calc(x_site, y_site)
    print(sum_out)
    
    # Жмакаем по списку, чтобы он раскрылся
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum_out))
    
    time.sleep(1)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    # time.sleep(1)
    
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

