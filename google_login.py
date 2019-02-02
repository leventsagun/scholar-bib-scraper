# https://stackoverflow.com/questions/48880646/python-selenium-use-a-browser-that-is-already-open-and-logged-in-with-login-cre

import pickle
import time 
from selenium import webdriver

def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

driver = webdriver.Chrome()
driver.get('http://www.scholar.google.com/');

sign_in = driver.find_element_by_partial_link_text('SIGN');
sign_in.click()

time.sleep(45) # finish login in before the end of this

driver.refresh()

save_cookie(driver, '/Users/leventsagun/GitHubProjects/G_logged_in')