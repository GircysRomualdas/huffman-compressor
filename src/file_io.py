
def read_text_file(path):
    content = ""

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    return content

def write_text_file(path, text):
    with open(path, 'w') as file:
        file.write(text)

def write_compressed_file(tree_str, bitstring, path):
    tree_bytes = tree_str.encode("utf-8")
    tree_len = len(tree_bytes)

    bit_len = len(bitstring)
    num_bytes = (bit_len + 7) // 8
    data_int = int(bitstring, 2)
    data_bytes = data_int.to_bytes(num_bytes, byteorder="big")

    with open(path + ".bin", "wb") as f:
        f.write(tree_len.to_bytes(4, byteorder="big"))
        f.write(tree_bytes)

        f.write(bit_len.to_bytes(4, byteorder="big"))
        f.write(data_bytes)

def read_compressed_file(path):
    with open(path, "rb") as f:
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
