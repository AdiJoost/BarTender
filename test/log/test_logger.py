import unittest
from unittest.mock import mock_open

class TestLogger(unittest.TestCase):

    def test_debug_LogLevelLow_logs(self):
        #ARRANGE
        self.assertEqual(1, 1)
        #ACT

        #ASSERT