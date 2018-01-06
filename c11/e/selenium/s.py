from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))
browser.get('http://115.28.34.230/login.do?type=gotoLogin')
accountElem = browser.find_element_by_name('userName')
accountElem.send_keys('hulianwang')
passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('123456')
passwordElem.submit()
