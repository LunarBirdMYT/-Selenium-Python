# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys('Здесь был Bob :)')
        
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

