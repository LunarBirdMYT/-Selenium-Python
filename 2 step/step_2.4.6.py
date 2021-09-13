from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    
    browser.implicitly_wait(5)
    button = browser.find_element_by_id("button")
    button.click()

finally:
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    browser.quit()