from unittest import TestCase

class TestSort_Tuple(TestCase):
    def test_Sort_Tuple(self):
        from Code.LeaderBoard import Sort_Tuple
        # is it working
        self.assertEqual(Sort_Tuple([("Tim",1)]), [("Tim",1)])
        # does it sort largest first
        self.assertEqual(Sort_Tuple([("Tim",1),("Ray",2)]), [("Ray",2),("Tim",1)])
