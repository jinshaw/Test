#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException
from time import  sleep ,ctime
import time
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://ecom-qa.baiwandian.cn/xinyunlian-weixin-ecom/wx/login.jhtml")


# try:
#         print (ctime())
#         driver.find_element_by_id("kw22").send_keys("selenium")
# except NoSuchElementException as e:
#         print(e)
# finally:
#         print (ctime())
#         driver.quit()

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("330405110441")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("1234")
driver.find_element_by_id("commonSubmit").click()
time.sleep(10)

title = driver.title
driver.assertEqual(title, u"新商盟")



driver.quit()