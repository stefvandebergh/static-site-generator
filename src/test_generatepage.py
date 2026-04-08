import unittest

from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# My Title\n\nThis is the content."
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_not_found(self):
        markdown = "This is the content without a title."
        with self.assertRaises(Exception):
            extract_title(markdown)