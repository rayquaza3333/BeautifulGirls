
from test_file import upcase_name
import unittest

class test_object(unittest.TestCase):
    def test1(self):
        text='Pham quang truong hoang'
        text=upcase_name(text)
        self.assertEqual(text,'Pham Quang Truong Hoang')
if __name__=="__main__":
    unittest.main()
