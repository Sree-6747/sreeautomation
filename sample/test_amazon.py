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
@pytest.fixture
def test_launch():
    #pass
    driver.get("https://www.amazon.in/")
@pytest.mark.parametrize("product,title",[("iphone","Amazon.in : iphone"),("oppo","Amazon.in : oppo"),("motto","Amazon.in : Mott")])
def test_title(product,title,test_launch):
    #driver.get("https://www.amazon.in/")

    driver.find_element(By.ID,"twotabsearchtextbox").send_keys(product)
    driver.find_element(By.ID, "nav-search-submit-button").click()
    assert driver.title == title,"title mismatch"

def test_url():
    print(driver.current_url)
    driver.quit()

