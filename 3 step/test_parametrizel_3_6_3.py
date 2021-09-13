import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def answer():
    return math.log(int(time.time()))
    # print(answer)

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/236{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(15)
    input1 = browser.find_element_by_css_selector(".textarea")
    input1.send_keys(str(answer()))
    click_send = WebDriverWait(browser, 120).until(
            EC.element_to_be_clickable((By.XPATH, 
                "//button[@class='submit-submission']")))
    click_send.click()
    
    WebDriverWait(browser, 120).until(
            EC.visibility_of_element_located((By.XPATH, 
                "//pre")))
    answer_text = browser.find_element_by_xpath('//pre')
    answer_checked = answer_text.text
    assert answer_checked != 'Correct!'
    