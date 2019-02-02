# # below is a sample copy from web
# import time 
# from selenium import webdriver
# driver = webdriver.Chrome()
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

#######################################################

import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options = webdriver.ChromeOptions()
# options.add_argument('user-data-dir=selenium') 
#Path to your chrome profile

# driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome()

driver.get('http://www.scholar.google.com/');
# then go ahead and manually login to the page 

sign_in = driver.find_element_by_partial_link_text('SIGN');
sign_in.click()

time.sleep(45)

FLAG = True

while FLAG:

	library = driver.find_element_by_partial_link_text('library');
	library.click()

	# time.sleep(1)
	with open('links.bib', 'a') as f:
		f.write(driver.current_url + '\n')

	select_all = driver.find_element_by_id('gs_res_ab_xall');
	select_all.click()

	# time.sleep(1)

	export = driver.find_element_by_id('gs_res_ab_exp-b');
	export.click()

	# time.sleep(1)

	bibtex = driver.find_element_by_partial_link_text('BibTeX');
	bibtex.click()

	# time.sleep(1)

	body = driver.find_element_by_tag_name('body');
	text = body.text 

	# time.sleep(1)

	with open('refs.bib', 'a') as f:
	    f.write(text + '\n\n')

	driver.back()

	# time.sleep(1)

	# driver.get('https://scholar.google.com/scholar?scilib=11&hl=en&as_sdt=0,5')

	try:
		next_button = driver.find_element_by_partial_link_text('Next');
		next_button.click()
	except:
		FLAG = False

