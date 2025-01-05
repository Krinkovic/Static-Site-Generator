import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is node", TextType.CODE, "www.silly.com")
        node2 = TextNode("This is node", TextType.CODE, "www.silly.com")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Heso", TextType.IMAGE)
        node2 = TextNode("Heso", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_not_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.idioticurl.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "www.idioticurl.com")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.idioticurl.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is a text node", TextType.CODE, "www.idioticurl.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "www.idioticurl.com")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()