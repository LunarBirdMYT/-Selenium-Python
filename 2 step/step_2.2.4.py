# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
    
try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';")
    time.sleep(5)
    
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

