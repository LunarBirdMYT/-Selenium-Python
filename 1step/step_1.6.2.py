# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id(By.ID, 'submit_button')