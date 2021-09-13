# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
from selenium import webdriver
# import time

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # В автотесте нам может понадобиться проверить, что для одного 
    # из radiobutton по умолчанию уже выбрано значение
    people_radio = browser.find_element_by_id("peopleRule")

    # Найдём атрибут "checked" с помощью встроенного метода get_attribute 
    # и проверим его значение:
    people_checked = people_radio.get_attribute('checked')
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
    # Проверим второй элемент
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    
    
finally:
    # успеваем скопировать код за 10 секунд
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

