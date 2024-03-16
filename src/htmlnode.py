class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_props = []
        if self.props:
            for key, value in self.props.items():
                html_props.append(f"{ key}='{value}'")
        return " ".join(html_props)
    
    def __repr__(self) -> str:
        print(self)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError
        elif not self.children:
            raise ValueError("The class ParentNode requires children")
        else:
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
            if not self.props:
                return f"<{self.tag}>{children_html}</{self.tag}>"
            else:
                return f"<{self.tag} {self.props_to_html()}>{children_html}</{self.tag}>"
                
