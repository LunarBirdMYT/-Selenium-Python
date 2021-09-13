# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
import time
import os
from selenium import webdriver



try:
    browser = webdriver.Chrome()

    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    print(current_dir)
    print(file_path)
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

