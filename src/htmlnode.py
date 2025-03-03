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

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
          
    def to_html(self):
        if self.value == None:
            raise ValueError("Value required")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag required")
        if self.children == None:
            raise ValueError("At least 1 child node required")
        
        print(self.props_to_html())
        return f"<{self.tag}{self.props_to_html()}>{children_to_html(self.children)}</{self.tag}>"

def children_to_html(child_list):
    if len(child_list) == 0:
        return ""
    print(child_list[0])
    children_string = ""
    children_string = child_list[0].to_html() + children_to_html(child_list[1:])
    print(children_string)
    return children_string

def main():
    node1 = LeafNode(None, "Hello").to_html()
    print(node1)
if __name__ == "__main__":
    main()