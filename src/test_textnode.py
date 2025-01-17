import unittest
from textnode import TextNode, TextType, text_node_to_html


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

    def test_text_to_html(self):
        node1 = TextNode("normal text", "text")
        node1_html = text_node_to_html(node1)
        self.assertEqual(node1_html, "normal text")

    def test_bold_to_html(self):
        node1 = TextNode("bold text", "bold")
        node1_html = text_node_to_html(node1)
        self.assertEqual(node1_html, "<b>bold text</b>")

    def test_italic_to_html(self):
        node1 = TextNode("italic text", "italic")
        node1_html = text_node_to_html(node1)
        self.assertEqual(node1_html, "<i>italic text</i>")

    def test_code_to_html(self):
        node1 = TextNode("if this then that: code", "code")
        node1_html = text_node_to_html(node1)
        self.assertEqual(node1_html, "<code>if this then that: code</code>")

    def test_link_to_html(self):
        node1 = TextNode("Link", "link", "www.a_link_here.com")
        node1_html = text_node_to_html(node1)
        self.assertEqual(node1_html, '<a href="www.a_link_here.com">Link</a>')

    def test_image_to_html(self):
        node1 = TextNode("A Beautiful Image", "image", "www.link_to_image.com")
        node1_html = text_node_to_html(node1)
        self.assertEqual(node1_html, '<img href="www.link_to_image.com" alt="A Beautiful Image"></img>')



if __name__ == "__main__":
    unittest.main()