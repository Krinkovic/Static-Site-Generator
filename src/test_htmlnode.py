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

    # write more tests here

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

    # write more tests here

class TestParentNode(unittest.TestCase):
    def test_repr(self):
        node1 = LeafNode("a", "Hey Asshole", {"href" : "www.testsite.com"})
        node2 = LeafNode("c", "Whatcha want", None)
        node3 = LeafNode("t", "Nothin", None)
        parent = ParentNode("p", [node1, node2, node3], {"class" : "testclass"})
        self.assertEqual(repr(parent), "HTMLNode(p, None, [LeafNode(a, Hey Asshole, None, {'href': 'www.testsite.com'}), LeafNode(c, Whatcha want, None, None), LeafNode(t, Nothin, None, None)], {'class': 'testclass'})")

    def test_eq(self):
        node1 = LeafNode("a", "Hey Asshole", {"href" : "www.testsite.com"})
        node2 = LeafNode("c", "Whatcha want", None)
        parent = ParentNode("p", [node1, node2], {"class" : "testclass"})
        parent2 = ParentNode("p", [node1, node2], {"class" : "testclass"})
        self.assertEqual(parent, parent2)
        
    def test_not_eq(self):
        node1 = LeafNode("a", "Hey Asshole", {"href" : "www.testsite.com"})
        node2 = LeafNode("c", "Whatcha want", None)
        node3 = LeafNode("c", "Whacha want", None)
        parent = ParentNode("p", [node1, node2], {"class" : "testclass"})
        parent2 = ParentNode("p", [node3, node2], {"class" : "testclass"})
        self.assertNotEqual(parent, parent2)

    def test_multiple_children(self):
        node1 = LeafNode("a", "Hey Asshole", {"href" : "www.testsite.com"})
        node2 = LeafNode("c", "Whatcha want", None)
        node3 = LeafNode("n", "Nothin", None)
        node4 = ParentNode("p", [node1, node2, node3], {"class" : "testclass"})
        self.assertEqual(node4.to_html(), '<p class="testclass"><a href="www.testsite.com">Hey Asshole</a><c>Whatcha want</c><n>Nothin</n></p>')

    def test_grandchildren(self):
        node1 = LeafNode("a", "Hey Asshole", {"href" : "www.testsite.com"})
        node2 = LeafNode("c", "Whatcha want", None)
        node3 = ParentNode("f", [node1, node2], None)
        node4 = ParentNode("p", [node3], {"class" : "testclass"})
        self.assertEqual(node4.to_html(), '<p class="testclass"><f><a href="www.testsite.com">Hey Asshole</a><c>Whatcha want</c></f></p>')

    # write more tests here

if __name__ == "__main__":
    unittest.main()