import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_text(self):
        node1 = TextNode("This is some **regular** text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node1], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode('This is some **regular** text', TextType.BOLD)])
    
    def test_bold(self):
        node1 = TextNode("This is some **test** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT), TextNode('test', TextType.BOLD), TextNode(' text', TextType.TEXT)])

    def test_double_bold(self):
        node1 = TextNode("This is some **test** text, and som more **test** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT), TextNode('test', TextType.BOLD), TextNode(' text, and som more ', TextType.TEXT), TextNode('test', TextType.BOLD), TextNode(' text', TextType.TEXT)])

    def test_italics(self):
        node1 = TextNode("This is some *test* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT), TextNode('test', TextType.ITALIC), TextNode(' text', TextType.TEXT)])

    def test_code(self):
        node1 = TextNode("This is some `test` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode('This is some ', TextType.TEXT), TextNode('test', TextType.CODE), TextNode(' text', TextType.TEXT)])

    def test_multi_type(self):
        node1 = TextNode("This *is* some **test** text", TextType.TEXT)
        nodes = split_nodes_delimiter([node1], "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(nodes, [TextNode('This ', TextType.TEXT, None), TextNode('is', TextType.ITALIC, None), TextNode(' some ', TextType.TEXT, None), TextNode('test', TextType.BOLD, None), TextNode(' text', TextType.TEXT, None)])

    def test_not_closed(self):
        node1 = TextNode("This is some *test text", TextType.TEXT)
        try:
            split_nodes_delimiter([node1], "*", TextType.ITALIC)
        except Exception as e:
            self.assertEqual("Invalid syntax. No closing delimiter", str(e))


if __name__ == "__main__":
    unittest.main()