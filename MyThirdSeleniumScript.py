from selenium import webdriver

chrome_path = "../chromedriver"

driver = webdriver.Chrome(chrome_path)
driver.get('http://vancouver.craigslist.com')
driver.find_element_by_xpath('//*[@id="sss0"]/li[23]/a').click()

posts = driver.find_elements_by_class_name('result-row')

for post in posts:
    print(post.text)
