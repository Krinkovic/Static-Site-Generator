import unittest
from textnode import TextNode, TextType
from inline_markdown import *

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

class TestText_Extraction(unittest.TestCase):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and this is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
 
    def test_image(self):
        self.assertEqual(extract_markdown_images(self.text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_link(self):
        self.assertEqual(extract_markdown_links(self.text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

class TestSplit_nodes_images(unittest.TestCase):

    def test_2nodes_4images(self):
        node1 = TextNode("This is text with an image of ![Rick & Morty](https://i.imagehub.com/aKaOqIh.gif) and the ![Teletubbies](https://i.photobomb.com/fJRm3Vk.jpeg)", TextType.TEXT)
        node2 = TextNode("This is text with a ![rick roll](https://i.imgur.com/gwur3nif09sd.gif) and ![obi wan](https://photobucket.com/picture.jpeg)", TextType.TEXT)
        old_nodes = [node1, node2]
        self.assertEqual(
            split_nodes_images(old_nodes),
            [
                "TextNode(This is text with an image of , TextType.TEXT, None)",
                "TextNode(Rick & Morty, TextType.IMAGE, https://i.imagehub.com/aKaOqIh.gif)",
                "TextNode( and the , TextType.TEXT, None)",
                "TextNode(Teletubbies, TextType.IMAGE, https://i.photobomb.com/fJRm3Vk.jpeg)",
                "TextNode(This is text with a , TextType.TEXT, None)",
                "TextNode(rick roll, TextType.IMAGE, https://i.imgur.com/gwur3nif09sd.gif)",
                "TextNode( and , TextType.TEXT, None)",
                "TextNode(obi wan, TextType.IMAGE, https://photobucket.com/picture.jpeg)"
            ]
        )
    def test_incorrect_format(self):
        pass
    def test3(self):
        pass
    def test4(self):
        pass
    def test5(self):
        pass
    def test6(self):
        pass
    def test7(self):
        pass
    def test8(self):
        pass
        

if __name__ == "__main__":
    unittest.main()