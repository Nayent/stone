import unittest
from programming.bill import Bill


class TestAmount(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(
            [
                'test1_email@test.com',
                'test2_email@test.com',
            ],
            {
                'banana': {
                    'quantity': 1,
                    'price': 100,
                },
                'apple': {
                    'quantity': 1,
                    'price': 200,
                }
            }
        )

    def test_normal_case(self):
        self.assertTrue(self.bill.validate_qnt_price())
    
    def test_negative_case_price(self):
        self.bill.shopping_list['banana']['price'] = -200
        self.assertRaises(Exception, lambda: self.bill.validate_qnt_price())
    
    def test_negative_case_quantity(self):
        self.bill.shopping_list['banana']['quantity'] = -1
        self.assertRaises(Exception, lambda: self.bill.validate_qnt_price())
    
    def test_equal(self):
        self.assertEqual(300, self.bill.price_all_items())
    
    def test_equal_zero(self):
        self.bill.shopping_list['banana']['quantity'] = 0
        self.bill.shopping_list['apple']['quantity'] = 0
        self.assertEqual(0, self.bill.price_all_items())