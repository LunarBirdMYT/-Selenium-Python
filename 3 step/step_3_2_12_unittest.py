import unittest
from selenium import webdriver
import time

browser = webdriver.Chrome()

class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        
        browser.get('http://suninjuly.github.io/registration1.html')
        
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
        self.assertEqual("Congratulations! You have successfully registered!",
                         welcome_text)
        
    def test_registration_2(self):
        browser.get('http://suninjuly.github.io/registration2.html')
        
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
        self.assertEqual("Congratulations! You have successfully registered!",
                         welcome_text)
        
        
if __name__ == "__main__":
    unittest.main()
 