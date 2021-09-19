import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket(browser):

    browser.get(link)
    assert browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary"), 'No such element! Please, find your error in code :)'