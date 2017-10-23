from count import Count
from count import Prime
import unittest
class TestCount(unittest.TestCase):

    def setUp(self):
        print ('test start')

    def test_add(self):
        j=Count(6,3)
        self.assertEqual(j.add(),5,msg='wrong')

    def test_prime(self):
        i=Prime(7)
        self.assertTrue(i.is_prime(),msg='is not prime!')

    def test_word(self):
        a="hello"
        b="hello world!"
        self.assertNotIn(a,b,msg="a is not in b")

    def tearDown(self):
        print ('test end')

class TestSub(unittest.TestCase):

    def setUp(self):
        print ('test sub start')

    def test_sub(self):
        a=Count(6,2)
        self.assertEqual(a.sub(),4)

    def tearDown(self):
        print ('test sub end')


if __name__=='__main__':
    # set up a test group
    suite = unittest.TestSuite()
    suite.addTest(TestSub("test_sub"))
    #run testcase
    runner=unittest.TextTestRunner()
    runner.run(suite)
    # unittest.main()