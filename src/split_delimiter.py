from htmlnode import *
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            subnodes = text.split(delimiter, 2)
            if len(subnodes) < 3:
                raise Exception("Invalid syntax. No closing delimiter")
            subnodes[0] = TextNode(subnodes[0], text_type)
            subnodes[2] = TextNode(subnodes[2], text_type)
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

def main():
    node1 = TextNode("This is some **test text**", TextType.TEXT)
    node2 = TextNode("This is some **test** text", TextType.BOLD)
    nodes = [node1, node2]
    new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    print(new_nodes)

if __name__ == "__main__":
    main()