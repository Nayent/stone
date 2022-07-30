import unittest
from programming.bill import Bill


class TestEmptyList(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(
            [
                'test1_email@test.com',
                'test2_email@test.com',
                'test3_email@test.com',
                'test4_email@test.com',
            ],
            {
                'banana': {
                    'quantidade': 1,
                    'preco': 100,
                }
            }
        )

    def test_normal_case(self):
        self.assertTrue(self.bill.validate_empty_list())
    
    def test_negative_case(self):
        self.bill.shopping_list = {}
        self.assertRaises(Exception, lambda: self.bill.validate_empty_list())