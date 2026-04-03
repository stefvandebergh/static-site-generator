from extractmarkdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text:
            continue
        matches = extract_markdown_images(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        new_nodes.extend(split_nodes_images_r(node.text, matches))
    return new_nodes

def split_nodes_images_r(node_text, matches):
    nodes = []
    if not matches:
        return [TextNode(f"{node_text}", TextType.TEXT)]
    alt_text, url = matches[0]
    node_text_split = node_text.split(f"![{alt_text}]({url})", 1)
    nodes.append(TextNode(f"{node_text_split[0]}", TextType.TEXT))
    nodes.append(TextNode(f"{alt_text}", TextType.IMAGE, f"{url}"))
    if len(node_text_split[1]) > 1:
        nodes.extend(split_nodes_images_r(node_text_split[1], matches[1:]))
    return nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text:
            continue
        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        new_nodes.extend(split_nodes_links_r(node.text, matches))
    return new_nodes

def split_nodes_links_r(node_text, matches):
    nodes = []
    if not matches:
        return [TextNode(node_text, TextType.TEXT)]
    link_text, url = matches[0]
    node_text_split = node_text.split(f"[{link_text}]({url})", 1)
    nodes.append(TextNode(node_text_split[0], TextType.TEXT))
    nodes.append(TextNode(link_text, TextType.LINK, url))
    if len(node_text_split[1]) > 1:
        nodes.extend(split_nodes_links_r(node_text_split[1], matches[1:]))
    return nodes

