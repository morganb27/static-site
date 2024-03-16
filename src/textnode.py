class TextNode:
    def __init__(self, text, txt_type, url=None):
        self.text = text
        self.txt_type = txt_type
        self.url = url
    
    def __eq__(self, __value: object) -> bool:
        return (self.text, self.txt_type, self.url) == (__value.text, __value.txt_type, __value.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.txt_type}, {self.url})"