# from selenium import webdriver

# browser = webdriver.Chrome()
# try:
#     browser.implicitly_wait(5)
    
#     browser.get("http://suninjuly.github.io/wait2.html")
    
#     button = browser.find_element_by_id("verify")
#     button.click()
#     message = browser.find_element_by_id("verify_message")
    
#     assert "successful" in message.text

# finally:
#     # После выполнения всех действий мы должны не забыть закрыть окно браузера
#     browser.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять в течение 15 секунд, пока цена дома не
    # уменьшится до $100
    if WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        ):
        button_book = browser.find_element_by_id('book')
        button_book.click()
    x_find = browser.find_element_by_id('input_value')
    x = x_find.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector('.form-control')
    input1.send_keys(y)
    button_submit = browser.find_element_by_id('solve')
    button_submit.click()

finally:
    time.sleep(10)
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    browser.quit()