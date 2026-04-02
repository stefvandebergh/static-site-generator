import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        node = LeafNode("p", props = {"href": "https://www.boot.dev"}, value="This is some anchor text")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is some anchor text")
        self.assertEqual(node.props, {"href": "https://www.boot.dev"})

    def test_props_to_html(self):
        node = LeafNode("a", props = {"href": "https://www.google.com","target": "_blank",}, value = "This is a Google link")
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = LeafNode("p", props = {"href": "https://www.google.com","target": "_blank",}, value="This is some anchor text")
        self.assertEqual(repr(node), '''HTMLNode with tag = p, value = This is some anchor text, properties =  href="https://www.google.com" target="_blank"''')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()