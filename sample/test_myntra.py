import time

import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
'''@pytest.fixture(scope='function')
def m1():
    print("this is fixture")
'''
@pytest.mark.order(1)

def test_launch():
    driver.get("https://www.myntra.com/")
@pytest.mark.order(3)

def test_title():
    print(driver.title)
    #assert driver.title=='STORE',"the test is fail"
@pytest.mark.order(2)

def test_url():
    print(driver.current_url)
    driver.quit()

