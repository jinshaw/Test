#-*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from time import sleep
class wxTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baiwandian.cn/xinyunlian-weixin-ecom/wx/login.jhtml")

    def login(self):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("17757190712")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("0001")
        driver.find_element_by_id("commonSubmit").click()
        time.sleep(10)

        title = driver.title
        self.assertEqual(title, u"中烟新商盟")

    def order(self):
        wxTest.login(self)
        driver = self.driver
        driver.find_element_by_class_name("searchMock").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='searchInp']").send_keys(u"测试商品")
        driver.find_element_by_id("searchBtn").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='productList']/li/div/div[6]/button[2]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("cart").click()
        time.sleep(10)
        driver.find_element_by_class_name("pay").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='orderInfo']/div[2]/div[7]/button[1]").click()
        time.sleep(10)
        location = driver.current_url
        self.assertEqual(location,"http://www.baiwandian.cn/xinyunlian-weixin-ecom/wx/index.jhtml")




    def tearDown(self):
        self.driver.quit()