from unittest import TestCase
from Lion import Lion
import unittest

class LionTest(TestCase):
    def test_init(self):
        st=Lion('hungry')
        self.assertEqual('hungry',st.state,'state error')

if __name__=='__main__':
    unittest.main()