#-*- coding: utf-8 -*-
import wxTest
import unittest
from HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(wxTest.wxTest("login"))
    suit.addTest(wxTest.wxTest("order"))
    filename = 'E:/WXreprot.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='test report',
                            description=u'微信商城用例执行情况')
    runner.run(suit)
    fp.close()