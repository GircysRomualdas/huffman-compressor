from node import Node, build_tree, sort_nodes, dfs_encode

from temp import *

def count_char(data_str):
    nodes = []

    for char in data_str:
        found = False

        for node in nodes:
            if node.char == char:
                node.count += 1
                found = True
                break

        if not found:
            nodes.append(Node(1, char))

    return nodes

def encode_test(data_str, code_map):
    encode_text = ""

    for char in data_str:
        encode_text += code_map[char]

    return encode_text

def decode_text(encoded_text, root_node):
    decode_text = ""
    node = root_node

    for char in encoded_text:
        if char == "0":
            node = node.left_node
        else:
            node = node.right_node

        if node.char is not None:
            decode_text += node.char
            node = root_node

    return decode_text

def main():
    nodes = count_char(test_data)
    sorted_nodes = sort_nodes(nodes)
    root_node = build_tree(sorted_nodes)
    code_map = dfs_encode(root_node)

    encoded_text = encode_test(test_data, code_map)
    decoded_text = decode_text(encoded_text, root_node)

    print(encoded_text)
    print("-------------------------")
    print(decoded_text)


if __name__ == "__main__":
    main()
