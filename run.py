#-*- coding: utf-8 -*-
import webDriverTest
import unittest
from HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':
    suit = unittest.TestSuite()
    #suit.addTest(webDriverTest.MyTest("login"))
    #suit.addTest(webDriverTest.MyTest("messageVerify"))
    suit.addTest(webDriverTest.MyTest("order"))
    filename = 'E:/reprot.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='test report',
                            description=u'PC商城用例执行情况')
    runner.run(suit)
    fp.close()