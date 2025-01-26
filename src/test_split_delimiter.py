import unittest
from split_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_bold(self):
        node1 = TextNode("This is some **test** text", TextType.TEXT)
        nodes = [node1]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        print(new_nodes)
        self.assertEqual(new_nodes)