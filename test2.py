# -*- coding: UTF-8 -*-
import unittest

class myTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip(u"直接跳过测试")
    def test_skip(self):
        print ("test aaa")

    @unittest.skipIf(3>2,"if result is ture,skip")
    def test_skip_if(self):
        print ("test bbb")

    @unittest.skipUnless(3>2,"unless result is ture,then skip")
    def test_skip_unless(self):
        print ("test ccc")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(3,3)

if __name__=='__main__':
    unittest.main()