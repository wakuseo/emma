from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'/home/tavershima/Documents/add_to_system_path ')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
