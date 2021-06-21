# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
import time
import math
from selenium import webdriver

link = "http://SunInJuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Отыскать элемент x на странице и расчитать уравнение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    answer = calc(x)
    
    # Найти область ввода и ввести ответ
    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(answer)
    
    # Кликнуть по области "Я робот"
    option1 = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           option1)
    option1.click()
    
    # Дальше нужно проскролить до выбора чекбокса и кликнуть)
    option2 = browser.find_element_by_css_selector('[id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           option2)
    option2.click()
    
    # Ну и остается кнопуля)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

