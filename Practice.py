from selenium import webdriver

print('Input your google email address')
userEmail = input()
print('Input your google password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('http://google.com')

loginElem = browser.find_element_by_link_text('Gmail')
loginElem.click()

loginElem = browser.find_element_by_link_text('Sign in')
loginElem.click()

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys(userEmail)

loginElem = browser.find_element_by_id('next')
loginElem.click()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(userPassword)
passwordElem.submit()

loginElem = browser.find_element_by_id('signIn')
loginElem.click()