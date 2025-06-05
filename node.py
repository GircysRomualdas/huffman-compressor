
class Node:
    def __init__(self, count, ascii_code = None, left_node = None, right_node = None):
        self.left_node = left_node
        self.right_node = right_node
        self.ascii_code = ascii_code
        self.count = count
        self.code = None

    def __str__(self):
        return f"<{self.ascii_code}> <{self.count}>"

def build_tree(nodes):
    if len(nodes) == 1:
        return nodes[0]

    new_nodes = []
    node_1 = nodes.pop(0)
    node_2 = nodes.pop(0)
    new_nodes.append(Node(node_1.count + node_2.count, None, node_1, node_2))
    new_nodes.extend(nodes)

    return build_tree(sort_nodes(new_nodes))

def sort_nodes(nodes):
    return sorted(nodes, key=lambda node: node.count)
