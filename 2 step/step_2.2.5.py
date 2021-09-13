# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
import time
from selenium import webdriver

link = "https://SunInJuly.github.io/execute_script.html"
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name("button")
    time.sleep(2)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

