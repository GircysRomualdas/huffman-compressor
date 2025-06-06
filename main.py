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

def read_text_data(path):
    content = ""

    with open(path, "r") as file:
        content = file.read()

    return content

def write_binary_data(encoded_tree, encoded_text, path):
    tree_bytes = encoded_tree.encode("utf-8")
    tree_len = len(tree_bytes)

    bit_len = len(encoded_text)
    num_bytes = (bit_len + 7) // 8
    data_int = int(encoded_text, 2)
    data_bytes = data_int.to_bytes(num_bytes, byteorder="big")

    with open(path + ".bin", "wb") as f:
        f.write(tree_len.to_bytes(4, byteorder="big"))
        f.write(tree_bytes)

        f.write(bit_len.to_bytes(4, byteorder="big"))
        f.write(data_bytes)

def read_binary_data(path):
    with open(path + ".bin", "rb") as f:
        tree_len_bytes = f.read(4)
        tree_len = int.from_bytes(tree_len_bytes, byteorder="big")
        tree_bytes = f.read(tree_len)
        encoded_tree = tree_bytes.decode("utf-8")

        bit_len_bytes = f.read(4)
        bit_len = int.from_bytes(bit_len_bytes, byteorder="big")
        num_bytes = (bit_len + 7) // 8
        data_bytes = f.read(num_bytes)
        data_int = int.from_bytes(data_bytes, byteorder="big")
        encoded_text = bin(data_int)[2:].rjust(bit_len, "0")

    return encoded_tree, encoded_text

def main():
    path = "data/Frankenstein.txt"
    test_data = read_text_data(path)
    nodes = count_char(test_data)
    sorted_nodes = sort_nodes(nodes)
    root_node = build_tree(sorted_nodes)
    code_map = dfs_encode(root_node)

    encoded_text = encode_test(test_data, code_map)
    encoded_tree = encode_tree(root_node)
    new_path = f"{path}.huff"

    write_binary_data(encoded_tree, encoded_text, new_path)
    bin_encoded_tree, bin_encoded_text = read_binary_data(new_path)

    bin_root_node = decode_tree(encoded_tree.strip().split())
    bin_decoded_text = decode_text(encoded_text, bin_root_node)

    print(bin_decoded_text)
    print(f"bin_encoded_tree: {bin_encoded_tree == encoded_tree}")
    print(f"bin_encoded_text: {bin_encoded_text == encoded_text}")

if __name__ == "__main__":
    main()
