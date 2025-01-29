import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node1 = TextNode("This is some **regular** text", TextType.BOLD)
        nodes = [node1]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode('This is some **regular** text', TextType.BOLD, None)])
    
    def test_bold(self):
        node1 = TextNode("This is some **test** text", TextType.TEXT)
        nodes = [node1]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT, None), TextNode('test', TextType.BOLD, None), TextNode(' text', TextType.TEXT, None)])

    def test_italics(self):
        node1 = TextNode("This is some *test* text", TextType.TEXT)
        nodes = [node1]
        new_nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT, None), TextNode('test', TextType.ITALIC, None), TextNode(' text', TextType.TEXT, None)])


if __name__ == "__main__":
    unittest.main()