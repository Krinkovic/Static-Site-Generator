import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node1 = TextNode("This is some **regular** text", TextType.BOLD)
        nodes = [node1]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode('This is some **regular** text', TextType.BOLD)])
    
    def test_bold(self):
        node1 = TextNode("This is some **test** text", TextType.TEXT)
        nodes = [node1]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT), TextNode('test', TextType.BOLD), TextNode(' text', TextType.TEXT)])

    def test_italics(self):
        node1 = TextNode("This is some *test* text", TextType.TEXT)
        nodes = [node1]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT), TextNode('test', TextType.ITALIC), TextNode(' text', TextType.TEXT)])


if __name__ == "__main__":
    unittest.main()