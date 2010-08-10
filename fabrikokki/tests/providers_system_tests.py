# Tests for fabrikokki/providers/system.py classes and functions
#
# NB: these are grouped into one file to mirror the current organization and
#     should be broken out to match whatever the layout eventually evolves
#     into.

# TODO: clean up imports, this is just copied from source file

import unittest
import fabrikokki

import grp
import os
import pwd
import subprocess
from kokki.base import Fail
from fabrikokki.providers.system import *


class Test(unittest.TestCase):
    """Unit tests for fabrikokki.providers.system"""

    def test_something(self):
        """Test fabrikokki"""
        gmaps = Kokki('test_recipes')
        result = something()
        self.assertEqual(result['titleNoFormatting'], 'Sushi Groove')


class TestFileProvider(unittest.TestCase):
    """Unit tests for FileProvider"""
    def test_something(self):
        self.assertEqual( False )


class TestDirectoryProvider(unittest.TestCase):
    """Unit tests for DirectoryProvider"""
    def test_something(self):
        self.assertEqual( False )


class TestLinkProvider(unittest.TestCase):
    """Unit tests for LinkProvider"""
    def test_something(self):
        self.assertEqual( False )


class TestExecuteProvider(unittest.TestCase):
    """Unit tests for ExecuteProvider"""
    def test_something(self):
        self.assertEqual( False )


class TestScriptProvider(unittest.TestCase):
    """Unit tests for ScriptProvider"""
    def test_something(self):
        self.assertEqual( False )


if __name__ == "__main__":
    unittest.main()