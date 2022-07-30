import unittest
from programming.bill import Bill

class TestDuplicateEmail(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(
            [
                'test1_email@test.com',
                'test2_email@test.com',
                'test3_email@test.com',
                'test4_email@test.com',
            ],
            {}
        )

    def test_normal_case(self):
        self.assertTrue(self.bill.validate_duplicate_email())
    
    def test_negative_case(self):
        self.bill.email_list.append('test1_email@test.com')
        self.assertRaises(Exception, lambda: self.bill.validate_duplicate_email())
    
    # def test_duplicate_email_v2(self):
    #     self.bill.email_list.append('test1_email@test.com')
    #     self.assertRaises(Exception, lambda: self.bill.validate_duplicate_email_v2())
    
    # def test_duplicate_email_v3(self):
    #     self.bill.email_list.append('test1_email@test.com')
    #     self.assertFalse(self.bill.validate_duplicate_email_v3())


if __name__ == "__main__":
        unittest.main()