from htmlnode import *
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        text = node.value
        subnodes = text.split(delimiter, 2)
        subnodes[0] = TextNode(subnodes[0], TextType.TEXT)
        subnodes[2] = TextNode(subnodes[2], TextType.TEXT)
        match delimiter:
            case "*":
                subnodes[1] = TextNode(subnodes[1], TextType.ITALIC)
            case "**":
                subnodes[1] = TextNode(subnodes[1], TextType.BOLD)
            case "`":
                subnodes[1] = TextNode(subnodes[1], TextType.CODE)
            case _:
                pass
        new_nodes.extend(subnodes)
    return new_nodes
        
    return subnodes

def main():
    node1 = LeafNode(None, "This is some **test** text")
    nodes = [node1]
    new_node = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    print(new_node)

if __name__ == "__main__":
    main()