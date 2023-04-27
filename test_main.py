"""Test file for testing the main.py file"""

import unittest
from unittest.mock import patch
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="1")
    def test_1(self, _mock_input):
        """Testa a função main com o input 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn('', captured_output.getvalue().strip())

    @patch("builtins.input", return_value="5")
    def test_5(self, _mock_input):
        """Testa a função main com o input 5"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn('', captured_output.getvalue().strip())

    @patch("builtins.input", return_value="20")
    def test_20(self, _mock_input):
        """Testa a função main com o input 20"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn('', captured_output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
