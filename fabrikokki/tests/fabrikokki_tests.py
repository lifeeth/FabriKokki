# Main fabrikokki tests

import unittest
from fabrikokki import Kokki

class Test(unittest.TestCase):
    """Unit tests for fabrikokki."""

    def test_local_search(self):
        """Test fabrikokki local_search()."""
        kokki = Kokki('test_recipes')
        self.assertEqual(result['titleNoFormatting'], 'Sushi Groove')

if __name__ == "__main__":
    unittest.main()