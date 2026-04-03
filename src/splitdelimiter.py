from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.texttype != TextType.TEXT:  
            new_nodes.append(node)
            continue
        new_node = node.text.split(delimiter)
        if delimiter not in node.text  :
            raise Exception(f"Delimiter '{delimiter}' not found in text: {node.text}")
        for i in range(len(new_node)):
            if i % 2 == 0:
                new_nodes.append(TextNode(new_node[i], node.texttype, node.url))
            else:
                new_nodes.append(TextNode(new_node[i], text_type, node.url))
    return new_nodes

