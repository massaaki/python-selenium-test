__author__ = 'Mauricio'

from selenium import webdriver


driver = webdriver.Chrome('../chromedriver')
driver.set_page_load_timeout(30)
driver.get('http://www.google.com')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file('Gogole.png')
driver.quit()
