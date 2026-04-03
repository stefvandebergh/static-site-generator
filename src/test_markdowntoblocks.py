import unittest

from markdowntoblocks import markdown_to_blocks



class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

        
    def test_markdown_to_blocks_empty_lines(self):
        md = """
This is a paragraph with empty lines before and after
This is another paragraph with empty lines before and after

- This is a list with empty lines before and after
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph with empty lines before and after\nThis is another paragraph with empty lines before and after",
                "- This is a list with empty lines before and after",
            ],
        )