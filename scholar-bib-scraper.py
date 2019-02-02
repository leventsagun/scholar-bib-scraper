# simple script to get bibtex entris of saved article in Google Scholer
# requires login and reCAPTCHA

import time 
from selenium import webdriver
from selenium.webdriver.support import ui


def get_entries_on_file(driver, log_file='links.txt', bib_file='refs.bib'):
    # all these sleeps may not be really necessary
    time.sleep(1)
    select_all = wait.until(lambda driver: driver.find_element_by_id('gs_res_ab_xall'))
    time.sleep(1)
    select_all.click()
    time.sleep(1)
    export = wait.until(lambda driver: driver.find_element_by_id('gs_res_ab_exp-b'))
    time.sleep(1)
    export.click()
    time.sleep(1)
    bibtex = wait.until(lambda driver: driver.find_element_by_partial_link_text('BibTeX'))
    time.sleep(1)
    bibtex.click()
    time.sleep(1)
    body = wait.until(lambda driver: driver.find_element_by_tag_name('body'))
    time.sleep(1)
    text = body.text 
    with open(bib_file, 'a') as f: # keep appending the bibtex entries to file
        f.write(text + '\n\n')
    with open(log_file, 'a') as f: # for logging
        f.write(driver.current_url + '\n')


if __name__ == '__main__':
    # initialize the browser -- requires chromedriver   
    driver = webdriver.Chrome()
    # this waiting may not be necessary
    wait = ui.WebDriverWait(driver, 90) 
    driver.get('http://www.scholar.google.com/');

    # complete login within 45 seconds
    sign_in = driver.find_element_by_partial_link_text('SIGN');
    sign_in.click()
    time.sleep(45) 

    library = wait.until(lambda driver: driver.find_element_by_partial_link_text('library'))
    time.sleep(1)
    library.click()

    time.sleep(90) # this is where I had to solve reCAPTCHA

    for i in range(1, 500): 
        # this loop breaks with some error after all done
        time.sleep(1)
        link = 'https://scholar.google.com/scholar?start={}&hl=en&as_sdt=0,5&scilib=1'.format(10*i)
        driver.get(link); # alt method: find and click NEXT until no longer can
        get_entries_on_file(driver)

