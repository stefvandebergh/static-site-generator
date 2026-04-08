from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type, BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from texttohtml import text_node_to_html_node
from texttotextnodes import text_to_textnodes

def markdown_to_html_node(md_doc):
    mdblocks = markdown_to_blocks(md_doc)
    parentnode = ParentNode("div", [], None)
    for block in mdblocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.HEADING:
                htmlnode = determine_heading_level(block)
            case BlockType.CODE:
                htmlnode = ParentNode("pre", [LeafNode("code", block[4:-3])], None)
            case BlockType.QUOTE:
                block = "\n".join(line.replace("> ", "", 1) for line in block.split("\n"))
                htmlnode = ParentNode("blockquote", text_to_children(block), None)
            case BlockType.PARAGRAPH:
                block = " ".join(line.strip() for line in block.split("\n"))
                htmlnode = ParentNode("p", text_to_children(block), None)
            case BlockType.UNORDERED_LIST:
                htmlnode = ParentNode("ul", [ParentNode("li", text_to_children(line[2:].strip()), None) for line in block.split("\n")], None)
            case BlockType.ORDERED_LIST:
                htmlnode = ParentNode("ol", [ParentNode("li", text_to_children(line[3:].strip()), None) for line in block.split("\n")], None)
        parentnode.children.append(htmlnode)
    return parentnode




def determine_heading_level(headingblock):
    for i in range(1, 7):
        if headingblock.startswith("#" * i + " "):
            return ParentNode("h" + str(i), text_to_children(headingblock[i + 1:].strip()), None)
        

def text_to_children(test):
    textnodes = text_to_textnodes(test)
    htmlnodes = []
    for textnode in textnodes:
        htmlnodes.append(text_node_to_html_node(textnode))
    return htmlnodes


# md = """
# > This is a blockquote
# > that spans multiple lines
# > and has **bold** and _italic_ text
#      """
# node = markdown_to_html_node(md)
# html = node.to_html()
# print(html)
# print("<div><blockquote>This is a blockquote that spans multiple lines and has <b>bold</b> and <i>italic</i> text</blockquote></div>")
