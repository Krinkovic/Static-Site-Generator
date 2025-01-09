import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Blahadiblaa", None, None)
        node2 = HTMLNode("h1", "Blahadiblaa", None, None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("h1", "Blahadiblaa", ["Gal Gadot", "Grim Fandango", "My Name is Earl"], None)
        node2 = HTMLNode("h1", "Blahadiblaa", None, None)
        self.assertNotEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("h1", "Blahadiblaa", None)
        node2 = LeafNode("h1", "Blahadiblaa", None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("a", "Blahadiblaa", {"href" : "www.testsite.com"})
        node2 = LeafNode("h1", "Blahadiblaa", None)
        self.assertNotEqual(node, node2)

class TestParentNode(unittest.TestCase):
    def test_test(self):
        node1 = LeafNode("a", "Blahadiblaa", {"href" : "www.testsite.com"})
        node2 = ParentNode("p", node1)
        self.assertEqual(node2.to_html, "testcase")

if __name__ == "__main__":
    unittest.main()