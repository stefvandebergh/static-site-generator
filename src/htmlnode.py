
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented for HTMLNode")

    def props_to_html(self):
        htmlstring = ""
        if not self.props:
            return ""
        for prop in self.props:
            htmlstring += f''' {prop}="{self.props[prop]}"'''
        return htmlstring

    def __repr__(self):
        return f"HTMLNode with tag = {self.tag}, value = {self.value}, children = {self.children}, properties = {self.props_to_html()}"