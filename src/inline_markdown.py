from htmlnode import *
from textnode import *
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception("Invalid syntax. No closing delimiter")
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_links_images(old_nodes):
#    if 1 == 1: return
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
# fix below this line
            sections = node.text.split()
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    pass
    for node in old_nodes:
        return old_nodes           
 
def split_nodes_link(old_nodes):
    pass

def main():
    node1 = TextNode("This is text with a ![Rick & Morty](https://i.imagehub.com/aKaOqIh.gif) and ![Teletubbies](https://i.photobomb.com/fJRm3Vk.jpeg)", TextType.TEXT)
    node2 = TextNode("This is text with a ![rick roll](https://i.imgur.com/gwur3nif09sd.gif) and ![obi wan](https://photobucket.com/picture.jpeg)", TextType.TEXT)
    old_nodes = [node1, node2]

    print(split_links_images(old_nodes))

    print(extract_markdown_images(node1))

if __name__ == "__main__":
    main()
