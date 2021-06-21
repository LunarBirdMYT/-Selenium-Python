# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, 'submit_button')
    button.click()
finally:
    # Закрываем браузер после всех манипуляций
    browser.quit()