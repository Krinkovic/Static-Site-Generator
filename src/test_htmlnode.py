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

    def test_repr(self):
        node = HTMLNode("h1", "Blahadiblaa", ["Gal Gadot", "Grim Fandango", "My Name is Earl"], None)
        self.assertEqual(repr(node), "HTMLNode(h1, Blahadiblaa, ['Gal Gadot', 'Grim Fandango', 'My Name is Earl'], None)")

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("h1", "Blahadiblaa", None)
        node2 = LeafNode("h1", "Blahadiblaa", None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("a", "Blahadiblaa", {"href" : "www.testsite.com"})
        node2 = LeafNode("h1", "Blahadiblaa", None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = LeafNode("a", "Blahadiblaa", {"href" : "www.testsite.com"})
        self.assertEqual(repr(node), "LeafNode(a, Blahadiblaa, None, {'href': 'www.testsite.com'})")


class TestParentNode(unittest.TestCase):
    def test_repr(self):
        node1 = LeafNode("a", "Hey Asshole", {"href" : "www.testsite.com"})
        node2 = LeafNode("c", "Whatcha want", None)
        node3 = LeafNode("t", "Nothin", None)
        parent = ParentNode("p", [node1, node2, node3], {"class" : "testclass"})
        self.assertEqual(repr(parent), "HTMLNode(p, None, [LeafNode(a, Hey Asshole, None, {'href': 'www.testsite.com'}), LeafNode(c, Whatcha want, None, None), LeafNode(t, Nothin, None, None)], {'class': 'testclass'})")

if __name__ == "__main__":
    unittest.main()