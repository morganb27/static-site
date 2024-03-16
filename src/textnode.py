from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, txt_type, url=None):
        self.text = text
        self.txt_type = txt_type
        self.url = url
    
    def __eq__(self, __value: object) -> bool:
        return (self.text, self.txt_type, self.url) == (__value.text, __value.txt_type, __value.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.txt_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.txt_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.txt_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.txt_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.txt_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.txt_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.txt_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.txt_type}")