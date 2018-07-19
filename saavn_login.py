#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

usrnm = raw_input('Enter username : ')
passwd = raw_input('Enter password : ')

playlist_name = raw_input('Enter playlist name : ')

driver = webdriver.Firefox()

driver.get('https://www.saavn.com/login.php?action=login')

element = driver.find_element_by_id("login_username")
element.clear()
element.send_keys(usrnm)

element = driver.find_element_by_id("login_password")
element.clear()
element.send_keys(passwd)

element = driver.find_element_by_id("static-login-btn")
element.click()

time.sleep(10)

element = driver.find_element_by_link_text(playlist_name)

driver.get(element.get_attribute("href"))

time.sleep(7)

elements = driver.find_elements_by_tag_name("meta")

links = []
for element in elements:
	try:
		if(element.get_attribute("property") == "music:song"):
			links.append(element.get_attribute("content"))
		
	except Exception as e:
		pass

f = open('song_names.txt','w')

for i in links:
	a = i.split('/')[-2]
	a = a.replace('-',' ')
	
	f.write(a)
	f.write('\n')
f.close()
driver.quit()

