from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,random

driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "http://sucai.redocn.com"
driver.get(base_url)

list=[
"433761",
"433989"
]

for numbers in list:
	print(numbers)
	time.sleep(random.randint(1,3))
	driver.find_element_by_id("keyword").click()
	driver.find_element_by_id("keyword").clear()
	driver.find_element_by_id("keyword").send_keys(numbers)
	try:
		driver.find_element_by_css_selector("fix-close").click()
	except:pass
	finally:
		driver.find_element_by_css_selector("input.search_btn").click()
		time.sleep(3)
		good_right=driver.find_element_by_css_selector("div.good_right")
		with open(numbers+'.txt','wb') as f:
			f.write(good_right.text)
		f.close()
		