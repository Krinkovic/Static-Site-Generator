import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), 'TextNode(This is a text node, TextType.BOLD, None)')

    def test_vals(self):
        node = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)

    def test_eq_url(self):
        node = TextNode("This is node", TextType.CODE, "www.silly.com")
        node2 = TextNode("This is node", TextType.CODE, "www.silly.com")
        self.assertEqual(node, node2)

    def test_eq_url_repr(self):
        node = TextNode("This is node", TextType.CODE, "www.silly.com")
        self.assertEqual(repr(node), 'TextNode(This is node, TextType.CODE, www.silly.com)')

    def test_eq_url_vals(self):
        node = TextNode("This is node", TextType.CODE, "www.silly.com")

        self.assertEqual(node.text, "This is node")
        self.assertEqual(node.text_type, TextType.CODE)
        self.assertEqual(node.url, "www.silly.com")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.idioticurl.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.someidioticurl.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()