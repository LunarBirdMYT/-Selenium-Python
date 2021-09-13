# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
import time
import os
from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Находим три поля ввода
    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys('Иван')
    
    input2 = browser.find_element_by_xpath('//input[@name="lastname"]')
    input2.send_keys('Иванов')
    
    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys('python@best.com')
    
    # Находим путь к нашему файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    # Отправляем файл
    send_form = browser.find_element_by_xpath('//input[@id="file"]')
    send_form.send_keys(file_path)
    
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()
    
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

