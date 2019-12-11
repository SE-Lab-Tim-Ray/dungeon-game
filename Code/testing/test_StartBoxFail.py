import unittest
import tkinter
from Code.Startbox import *
class TestStartbox(unittest.TestCase):
    def setUp(self):
        self.root=tkinter.Tk()
        self.pump_events()
    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()
    def pump_events(self):
        while self.root.DoOneEvent(tkinter.ALL_EVENTS | tkinter.DONT_WAIT):
            pass
class TestInput(TestStartbox):
    def test_enter(self):
        import startbox from Code.Startbox
        startbox = startbox(self.root, value=u"abc")
        self.pump_events()
        startbox.e.focus_set()
        startbox.e.event_generate('<Return>')
        self.pump_events()
        self.assertRaises(tkinter.TclError, lambda: startbox.top.winfo_viewable())
        self.assertEqual(startbox.value, "abc")

if __name__=='__main__':
    unittest.main()

