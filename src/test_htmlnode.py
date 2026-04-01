import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        node = HTMLNode("p", props = {"href": "https://www.boot.dev"}, value="This is some anchor text")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is some anchor text")
        self.assertEqual(node.props, {"href": "https://www.boot.dev"})

    def test_props_to_html(self):
        node = HTMLNode("a", props = {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p", props = {"href": "https://www.google.com","target": "_blank",}, value="This is some anchor text")
        self.assertEqual(repr(node), '''HTMLNode with tag = p, value = This is some anchor text, children = None, properties =  href="https://www.google.com" target="_blank"''')


if __name__ == "__main__":
    unittest.main()