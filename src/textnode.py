from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		return (
			self.text == other.text
			and self.text_type == other.text_type
			and self.url == other.url
		)

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html(textnode):
	match (textnode.text_type):
		case "text":
			return LeafNode(None, textnode.text).to_html()
		case "bold":
			return LeafNode("b", textnode.text).to_html()
		case "italic":
			return LeafNode("i", textnode.text).to_html()
		case "code":
			return LeafNode("code", textnode.text).to_html()
		case "link":
			return LeafNode("a", textnode.text, {"href" : textnode.url}).to_html()
		case "image":
			return LeafNode("img", "", {"href" : textnode.url, "alt" : textnode.text}).to_html()
		case _:
			raise Exception("No valid text type")