
class Node:
    def __init__(self, count, char = None, left_node = None, right_node = None):
        self.left_node = left_node
        self.right_node = right_node
        self.char = char
        self.count = count

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

def dfs_encode(node, code="", code_map=None):
    if code_map is None:
        code_map = {}

    if node:
        if node.char is not None:
             code_map[node.char] = code

        dfs_encode(node.left_node, code + "0", code_map)
        dfs_encode(node.right_node, code + "1", code_map)

    return code_map

def encode_tree(node):
    if node.char is not None:
        return f"L:{ord(node.char)}"
    return "N " + encode_tree(node.left_node) + " " + encode_tree(node.right_node)

def decode_tree(tokens):
    tokens_iter = iter(tokens)

    def helper():
        token = next(tokens_iter)

        if token.startswith("L:"):
            char = chr(int(token[2:]))
            return Node(0, char)

        elif token == "N":
            left_node = helper()
            right_node = helper()
            return Node(0, None, left_node, right_node)

        else:
            raise ValueError(f"Invalid token: {token}")

    return helper()
