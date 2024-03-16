import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props_dict = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props_dict)
        expected_output =  "href='https://www.google.com' target='_blank'"
        self.assertEqual(HTMLNode.props_to_html(node), expected_output)

    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_output = "<p>This is a paragraph of text.</p>"
        self.assertEqual(LeafNode.to_html(node), expected_output)

    def test_to_html_no_tags(self):
        node = LeafNode(None, "This is some text with no tags.")
        expected_output = "This is some text with no tags."
        self.assertEqual(LeafNode.to_html(node), expected_output)

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_output = "<a href='https://www.google.com'>Click me!</a>"
        self.assertEqual(LeafNode.to_html(node), expected_output)
    
    def test_to_html_with_no_value(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            LeafNode.to_html(node)
        

    

if __name__ == "__main__":
    unittest.main()

    
