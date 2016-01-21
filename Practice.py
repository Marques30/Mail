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

btnElem = browser.find_element_by_link_text('Mail')
btnElem.click()

emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys(userPassword)
passwordElem.submit()

loginElem = browser.find_element_by_id('login-signin')
loginElem.click()

skipElem = browser.find_element_by_id('skipbtn')
skipElem.click()

composeElem = browser.find_element_by_id('Compose')
composeElem.click()

reElem = browser.find_element_by_id('to-field')
reElem.send_keys(userSender)

subElem = browser.find_element_by_id('subject-field')
subElem.send_keys(userSubject)

sendElem = browser.find_element_by_link_text('Send')
sendElem.click()