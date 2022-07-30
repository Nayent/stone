import unittest
from programming.bill import Bill


class TestSplit(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(
            [
                'test1_email@test.com',
                'test2_email@test.com',
                'test3_email@test.com',
            ],
            {
                'banana': {
                    'quantity': 1,
                    'price': 100,
                }
            }
        )

    def test_case_100_3(self):
        self.assertEqual(
            {
                'test1_email@test.com': 34,
                'test2_email@test.com': 33,
                'test3_email@test.com': 33,
            },
            self.bill.split()
        )
    
    def test_case_102_4(self):
        self.bill.email_list.append('test4_email@test.com')
        self.bill.shopping_list['banana']['price'] = 102
        self.assertEqual(
            {
                'test1_email@test.com': 26,
                'test2_email@test.com': 26,
                'test3_email@test.com': 25,
                'test4_email@test.com': 25,
            },
            self.bill.split()
        )
    
    def test_case_1_3(self):
        self.bill.shopping_list['banana']['price'] = 1
        self.assertEqual(
            {
                'test1_email@test.com': 1,
                'test2_email@test.com': 0,
                'test3_email@test.com': 0,
            },
            self.bill.split()
        )
    