from enum import Enum

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 6
    IMAGE = 7


class TextNode:
    def __init__(self, text, texttype, url= None):
        self.text = text
        self.texttype = texttype
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.texttype == other.texttype and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.texttype}, {self.url})"