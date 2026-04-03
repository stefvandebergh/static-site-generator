from splitnodes import split_nodes_images, split_nodes_links
from splitdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

def text_to_textnodes(text):
    delimiters = {
        "_": TextType.ITALIC,
        "**": TextType.BOLD,
        "`": TextType.CODE
    }
    returnnodes = [TextNode(text, TextType.TEXT)]

    for delimiter in delimiters:
        if delimiter in text:
            returnnodes = split_nodes_delimiter(returnnodes, delimiter, delimiters[delimiter])
    return split_nodes_images(split_nodes_links(returnnodes))