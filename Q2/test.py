import unittest
from CompareVersion import CompareVersion


class TestCompareVersion(unittest.TestCase):    

    def test_compare_v1_greater_than_v2(self):
        testing = CompareVersion()
        self.assertEqual(testing.compare_version('1.2.1.87','1.2.1.45'), 1, "{} should be > {}".format('1.2.1.87','1.2.1.45'))
        self.assertEqual(testing.compare_version('4.3.1.60','3.2.1.60'), 1, "{} should be > {}".format('4.3.1.60','3.2.1.60'))
        self.assertEqual(testing.compare_version('2.4.3.30','2.4.3.1'), 1, "{} should be > {}".format('2.4.3.30','2.4.3.1'))
        self.assertEqual(testing.compare_version('8.4.3.30','2.5.3.1'), 1, "{} should be > {}".format('8.4.3.30','2.5.3.1'))
    
    def test_compare_v2_greater_than_v1(self):
        testing = CompareVersion()
        self.assertEqual(testing.compare_version('6.7.37','6.7.37.80.456'), -1, "{} should be > {}".format('6.7.37.80.456','6.7.37'))
        self.assertEqual(testing.compare_version('2','6.3.1'), -1, "{} should be > {}".format('6.3.1','2'))
        self.assertEqual(testing.compare_version('0.0.0.0.1','2.4.3.30'), -1, "{} should be > {}".format('2.4.3.30','0.0.0.0.1'))
        self.assertEqual(testing.compare_version('123.3432.545234.34','232.34324.123.343'), -1, "{} should be > {}".format('123.3432.545234.34','232.34324.123.343'))

    def test_compare_v1_equal_to_v2(self):
        testing = CompareVersion()
        self.assertEqual(testing.compare_version('1','1'), 0, "{} should be == {}".format('1','1'))
        self.assertEqual(testing.compare_version('1.0.01.01','1.0.1.1'), 0, "{} should be == {}".format('1.0.01.01','1.0.1.1'))
        self.assertEqual(testing.compare_version('5','5.0.0.0.0.0.0.0'), 0, "{} should be == {}".format('5','5.0.0.0.0.0.0.0'))
        self.assertEqual(testing.compare_version('010.56.34.0954','10.56.34.954'), 0, "{} should be == {}".format('010.56.34.0954','10.56.34.954'))
        
            

if __name__ == '__main__':
    unittest.main()