# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # находим элемент "х" по его айди, затем преобразуем это в текст
    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)
    
    # Находим элемент текстового поля и вставляем рассчитанное значение
    input1 = browser.find_element_by_xpath('//input[@class="form-control"]')
    input1.send_keys(y)

    # Теперь идем по кнопулям ради о чекбоксам
    option1 = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    option1.click()
    
    time.sleep(1)
    
    option2 = browser.find_element_by_css_selector('[for="robotsRule"]')
    option2.click()    
    
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

