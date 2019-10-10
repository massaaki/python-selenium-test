__author__ = 'Mauricio'

from selenium import webdriver


driver = webdriver.Chrome('../chromedriver')
driver.set_page_load_timeout(30)
driver.get('http://www.google.com')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("..\\Screenshots\\Google0.png")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('hello world')
driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[1]/div[3]/center/input[1]').click()
driver.get_screenshot_as_file("..\\Screenshots\\Google1.png")
driver.quit()
