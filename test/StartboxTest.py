import unittest

from Code.Startbox import *
class testStartBox(unittest.TestCase):
    def test_startbox(self):
        startbox()
    def test_input(self):
        self.assertEqual(startbox(), 'abc', 'abc')
        self.assertEqual(startbox(), '123', '123')
        self.assertEqual(startbox(), 'Alan', 'Alan')
        self.assertEqual(startbox(), 'Alan1', 'Alan2')
        self.assertEqual(startbox(), 'Alan_4', 'Alan_4')

if __name__=='__main__':
    unittest.main()
