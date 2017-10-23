#-*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
from time import sleep
from selenium.webdriver.remote import webelement
import MySQLdb
from selenium.webdriver.common.keys import Keys

class MyTest(unittest.TestCase):


    def setUp(self):

        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baiwandian.cn/xinyunlian-ecom/login/dl.jhtml")

    #登录
    def login(self):
        driver = self.driver
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("17757190712")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("0001")
        driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/div[2]/div[2]/input").click()
        title = driver.title
        self.assertEqual(title, u"新商盟")

    def messageVerify(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/div[2]/ul/li[2]").click()
        #driver.find_element_by_name("username").clear()
        sleep(5)
        driver.find_element_by_xpath("//*[ @ id = 'passwordForm']/div[2]/div/input").send_keys("17757190712")
        driver.find_element_by_id("getDyPassword").click()

    def order(self):
        driver = self.driver
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("17757190712")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("0001")
        driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/div[2]/div[2]/input").click()
        time.sleep(10)
        driver.find_element_by_name("keyword").send_keys(u"测试商品")
        driver.find_element_by_class_name("search-btn").click()
        driver.find_element_by_xpath("//*[@id='product-list']/div[1]/ul/li[8]/button[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/a[2]").click()
        driver.find_element_by_xpath("//*[@id='cart-list']/div[4]/input").click()
        time.sleep(10)
        elem = driver.find_element_by_xpath("//*[@id='submit']")
        elem.send_keys(Keys.ENTER)
        # 验证下单后
        title = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]")
        self.assertIsNotNone(title, "not found")



    def tearDown(self):
        self.driver.quit()




# #搜索商品
# keyword=u"可乐".encode("utf-8")
# driver.find_element_by_name("keyword").clear()
# driver.find_element_by_name("keyword").send_keys(u"可乐")
# driver.find_element_by_class_name("search-btn").click()
