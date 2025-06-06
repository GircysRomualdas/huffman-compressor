from node import Node, build_tree, sort_nodes, dfs_encode, encode_tree, decode_tree

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

def read_data(path):
    content = ""

    with open(path, "r") as file:
        content = file.read()

    return content

def write_data(path, text):
    with open(path, "w") as file:
        file.write(text)

def main():
    path = "data/Frankenstein.txt"
    test_data = read_data(path)
    nodes = count_char(test_data)
    sorted_nodes = sort_nodes(nodes)
    root_node = build_tree(sorted_nodes)
    code_map = dfs_encode(root_node)

    encoded_text = encode_test(test_data, code_map)
    encoded_tree = encode_tree(root_node)
    full_text = f"{encoded_tree}\n{encoded_text}"
    new_path = f"{path}.huff"
    write_data(new_path, full_text)

    full_encoded_text = read_data(new_path).split("\n")
    encoded_tree = full_encoded_text[0]
    encoded_text = full_encoded_text[1]

    root = decode_tree(encoded_tree.strip().split())
    decoded_text = decode_text(encoded_text, root)

    print(decoded_text)


if __name__ == "__main__":
    main()
