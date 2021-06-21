# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:48:46 2021

@author: Оператор
"""
from selenium import webdriver
import time

menu = int(input(
    'Введите цифру в зависимости от того, какую ссылку запустить: \n \
             1 - http://suninjuly.github.io/registration1.html \n \
             2 - http://suninjuly.github.io/registration2.html \n \
Мой выбор: '))
if menu == 1:
    link = 'http://suninjuly.github.io/registration1.html'
elif menu == 2:
    link = 'http://suninjuly.github.io/registration2.html'
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_xpath(
        '//div[@class="first_block"]/div[@class="form-group first_class"]/ \
            input[@class="form-control first"]'
            )
    input1.send_keys('Ivan')
    input2 = browser.find_element_by_xpath(
        '//div[@class="first_block"]/div[@class="form-group second_class"]/ \
            input[@class="form-control second"]'
            )
    input2.send_keys('Petrov')
    input3 = browser.find_element_by_xpath(
        '//div[@class="first_block"]/div[@class="form-group third_class"]/ \
            input[@class="form-control third"]'
            )
    input3.send_keys('pav@mail.ru')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

