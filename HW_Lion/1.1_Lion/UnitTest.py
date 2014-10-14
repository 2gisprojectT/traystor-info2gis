from unittest import TestCase
from Lion import Lion
import unittest

class LionTest(TestCase):
    def test_hungry(self):
        lion = Lion('hungry')
        self.assertEqual('hungry',lion .state,'state error')

    def test_full(self):
        lion = Lion('full')
        self.assertEqual('full', lion .state, 'state error')

if __name__=='__main__':
    unittest.main()