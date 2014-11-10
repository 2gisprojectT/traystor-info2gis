from unittest import TestCase
from lion import Lion
import unittest

class LionTestFull(TestCase):
    def test_full(self):
        lionState = Lion('full')
        self.assertEqual('full', lionState.state, 'state error')

    def test_antilopa_full(self):
        lionState = Lion('full')
        self.assertEqual('Lion sleep', lionState.antilopa(), 'state error')

    def test_hunter_full(self):
        lionState = Lion ('full')
        self.assertEqual('Run Lion, RUN!', lionState.hunter(), 'state error')

    def test_tree_full(self):
        lionState = Lion ('full')
        self.assertEqual('Lion see on tree', lionState.tree(), 'state error')

class LionTestHungry(TestCase):

    def test_hungry(self):
        lionState = Lion('hungry')
        self.assertEqual('hungry', lionState.state, 'state error')

    def test_antilopa_hungry(self):
        lionState = Lion('hungry')
        self.assertEqual('Lion eat', lionState.antilopa(), 'state error')

    def test_hunter_hungry(self):
        lionState = Lion ('hungry')
        self.assertEqual('Run Lion, RUN!', lionState.hunter(), 'state error')

    def test_tree_hungry(self):
        lionState = Lion ('hungry')
        self.assertEqual('Lion sleep', lionState.tree(), 'state error')

if __name__=='__main__':
    unittest.main()