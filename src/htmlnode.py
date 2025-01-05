class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return (
			self.tag == other.tag
			and self.value == other.value
			and self.children == other.children
            and self.props == other.props
		)
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_string = ""
        for prop in self.props:
            props_string = props_string + f' {prop}="{self.props[prop]}"'
        return props_string
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Value required")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

def main():

    testnode = LeafNode("a", "Hello assholes!", {"href" : "www.assholes.com"})
    testnode2 = LeafNode("a", "Hello assholes!", {"href" : "www.assholes.com", "layout" : "ugly"})
    testnode3 = LeafNode("p", "Hello Muthafuckas!")

    print(testnode.to_html())
    print(testnode2.to_html())
    print(testnode3.to_html())

if __name__ == "__main__":
    main()