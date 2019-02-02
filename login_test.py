# https://stackoverflow.com/questions/48880646/python-selenium-use-a-browser-that-is-already-open-and-logged-in-with-login-cre

import pickle
import time 
from selenium import webdriver

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)


driver = webdriver.Chrome()
load_cookie(driver, '/Users/leventsagun/GitHubProjects/G_logged_in')

driver.get('http://www.scholar.google.com/');

library = driver.find_element_by_partial_link_text('library');
library.click()
