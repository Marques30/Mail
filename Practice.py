from selenium import webdriver

print('Input your yahoo email address')
userEmail = input()
print('Input your yahoo password')
userPassword = input()
print('Input who you are sending to')
userSender = input()
print('Input the subject of email')
userSubject = input()

browser = webdriver.Firefox()
browser.get('http://yahoo.com')

loginElem = browser.find_element_by_link_text('Mail')
loginElem.click()

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys(userPassword)
passwordElem.submit()

loginElem = browser.find_element_by_id('login-signin')
loginElem.click()

loginElem = browser.find_element_by_id('skipbtn')
loginElem.click()

loginElem = browser.find_element_by_partial_link_text('Compose')
loginElem.click()

emailElem = browser.find_element_by_id('to-field')
emailElem.send_keys(userSender)

emailElem = browser.find_element_by_id('subject-field')
emailElem.send_keys(userSubject)

loginElem = browser.find_element_by_link_text('Send')
loginElem.click()