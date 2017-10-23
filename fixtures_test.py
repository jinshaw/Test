import  unittest

def setUpModle():
    print ("test module start >>>>>>>>")


def tearDownModle():
    print ("test module end >>>>>>>>")

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("test class start >>>>>>>")
    @classmethod
    def tearDownClass(cls):
        print ("test class end >>>>>")

    def setUp(self):
        print ("test case start >>>>>")

    def tearDown(self):
        print ("test case end >>>>>>")

    def test_case(self):
        print ("test case 1")

    def test_case2(self):
        print ("test case 2")

if __name__ == '__main__':
    unittest.main()
