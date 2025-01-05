import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode("h1", "Blahadiblaa", None, None)
        node2 = HTMLNode("h1", "Blahadiblaa", None, None)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode("h2", "Blahadiblaa", None, None)
        node2 = HTMLNode("h2", "Blahadiblaa", None, None)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = HTMLNode("h1", "Blahadiblaa", None, {"heso" : "peso"})
        node2 = HTMLNode("h1", "Blahadiblaa", None, {"heso" : "peso"})
        self.assertEqual(node, node2)

    def test_not_eq1(self):
        node = HTMLNode("h1", "Blahadiblaa", ["Gal Gadot", "Grim Fandango", "My Name is Earl"], None)
        node2 = HTMLNode("h1", "Blahadiblaa", None, None)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = HTMLNode("h1", "Blahadiblaa", None, None)
        node2 = HTMLNode("h1", "Blahadiblaa", None, {"heso" : "peso", "pi" : 3.14})
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = HTMLNode("h1", "Blöhööö", None, None)
        node2 = HTMLNode("h1", "Blahadiblaa", None, None)
        self.assertNotEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    def test_eq1(self):
        node = LeafNode("h1", "Blahadiblaa", None)
        node2 = LeafNode("h1", "Blahadiblaa", None)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = LeafNode("h2", "Blahadiblaa", None)
        node2 = LeafNode("h2", "Blahadiblaa", None)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = LeafNode("h1", "Blahadiblaa", {"heso" : "peso"})
        node2 = LeafNode("h1", "Blahadiblaa", {"heso" : "peso"})
        self.assertEqual(node, node2)

    def test_not_eq1(self):
        node = LeafNode("a", "Blahadiblaa", {"href" : "www.testsite.com"})
        node2 = LeafNode("h1", "Blahadiblaa", None)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = LeafNode("h1", "Blahadiblaa", None)
        node2 = LeafNode("h1", "Blahadiblaa", {"heso" : "peso", "pi" : 3.14})
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = LeafNode("h1", "Blöhööö", None)
        node2 = LeafNode("h1", "Blahadiblaa", None)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()