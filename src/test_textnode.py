import unittest

from textnode import TextNode, LeafNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "example.com")
        expected_repr = "TextNode(This is a text node, bold, example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", "bold")
        expected_output = LeafNode("b", "Hello, world!")  
        actual_output = text_node_to_html_node(text_node)
        self.assertEqual(repr(actual_output), repr(expected_output))





if __name__ == "__main__":
    unittest.main()

    
