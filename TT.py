# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import os

driver=webdriver.Chrome()
driver.get("http://myhengtian/")
#登录
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("jinxiao")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("Shaw@1117")
driver.find_element_by_name("submit").click()
#driver.switch_to.alert.accept()
#打开TT
driver.find_element_by_id("urlTts").click()
#打开新页面后定位元素到新页面
driver.switch_to_window(driver.window_handles[-1])
#搜索元素
'''
while 1:
    start = time.clock()
    try:
        driver.find_element_by_link_text("Daily Report").click()
        print '已定位到元素'
        end=time.clock()
        break
    except:
        print "还未定位到元素!"

print '定位耗费时间：'+str(end-start)
'''
driver.find_element_by_link_text("Daily Report").click()
#新增TT
driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbNewDailyReport").click()
driver.switch_to_window(driver.window_handles[-1])
time.sleep(3)
#输入TT内容
driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_tbDescription']").send_keys(u"云小钱测试和团购抽奖测试")
#点击新增
driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnCommit").click()

driver.quit()
