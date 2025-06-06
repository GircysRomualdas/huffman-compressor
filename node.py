
class Node:
    def __init__(self, count, character = None, left = None, right = None):
        self.left = left
        self.right = right
        self.character = character
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

def build_encoding_map(node, code="", encoding_map=None):
    if encoding_map is None:
        encoding_map = {}

    if node:
        if node.character is not None:
             encoding_map[node.character] = code

        build_encoding_map(node.left, code + "0", encoding_map)
        build_encoding_map(node.right, code + "1", encoding_map)

    return encoding_map

def serialize_tree(node):
    if node.character is not None:
        return f"L:{ord(node.character)}"
    return "N " + serialize_tree(node.left) + " " + serialize_tree(node.right)

def deserialize_tree(tokens):
    tokens_iter = iter(tokens)

    def helper():
        token = next(tokens_iter)

        if token.startswith("L:"):
            character = chr(int(token[2:]))
            return Node(0, character)
        elif token == "N":
            left_node = helper()
            right_node = helper()
            return Node(0, None, left_node, right_node)
        else:
            raise ValueError(f"Error while decoding tree: invalid token '{token}'. The file may be corrupted or not a valid Huffman binary.")


    return helper()
