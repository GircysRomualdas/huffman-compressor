from node import Node, build_tree, sort_nodes, build_encoding_map, serialize_tree, deserialize_tree
import sys
import os

def get_character_frequencies(text):
    nodes = []

    for character in text:
        found = False

        for node in nodes:
            if node.character == character:
                node.count += 1
                found = True
                break

        if not found:
            nodes.append(Node(1, character))

    return nodes

def encode_text_to_bits(text, encoding_map):
    encoded_text = ""

    for character in text:
        encoded_text += encoding_map[character]

    return encoded_text

def decode_bits_to_text(encoded_bits, root):
    decoded_text = ""
    node = root

    for character in encoded_bits:
        if character == "0":
            node = node.left
        else:
            node = node.right

        if node.character is not None:
            decoded_text += node.character
            node = root

    return decoded_text

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

def compress_file(path):
    text_data = read_text_file(path)
    if not text_data:
        raise ValueError("Error: File is empty. Nothing to compress.")

    character_nodes = get_character_frequencies(text_data)
    sorted_nodes = sort_nodes(character_nodes)
    tree_root = build_tree(sorted_nodes)
    encoding_map = build_encoding_map(tree_root)
    encoded_bitstring = encode_text_to_bits(text_data, encoding_map)
    serialized_tree = serialize_tree(tree_root)
    output_path = f"{path}.huff"
    write_compressed_file(serialized_tree, encoded_bitstring, output_path)

    original_size = len(text_data.encode("utf-8"))
    compressed_size = len(encoded_bitstring) // 8
    return output_path, original_size, compressed_size

def decompress_file(path):
    serialized_tree, bitstring = read_compressed_file(path)
    root_node = deserialize_tree(serialized_tree.strip().split())
    decoded_text = decode_bits_to_text(bitstring, root_node)
    output_path = f"{path.removesuffix(".huff.bin")}.huff"
    write_text_file(output_path, decoded_text)
    return output_path

def main():
    try:
        flag = sys.argv[1]
        path = sys.argv[2]
    except IndexError:
        print("Usage:")
        print("    python main.py compress   <file.txt>")
        print("    python main.py decompress <file.txt.huff.bin>")
        sys.exit(1)

    try:
        if not os.path.exists(path):
            raise FileNotFoundError

        match flag:
            case "compress":
                new_path, original_size, compressed_size = compress_file(path)
                print(f"[✓] Compression successful!")
                print(f"    Original file:     {path}")
                print(f"    Compressed file:   {new_path}")
                print(f"    Original size:     {original_size} bytes")
                print(f"    Compressed size:   {compressed_size} bytes")
                print(f"    Compression ratio: {compressed_size/original_size:.2%}")
            case "decompress":
                if not path.endswith(".huff.bin"):
                    raise ValueError("Error: Invalid file suffix for decompression.")

                new_path = decompress_file(path)
                size = os.path.getsize(new_path)
                print(f"[✓] Decompression successful!")
                print(f"    Input file:        {path}")
                print(f"    Output file:       {new_path}")
                print(f"    Decompressed size: {size} bytes")
            case _:
                print("Error: Invalid flag. Use 'compress' or 'decompress'")
                sys.exit(1)
    except FileNotFoundError:
        print(f"[X] Error: File '{path}' not found.")
        sys.exit(1)
    except ValueError as ve:
        print(f"[X] {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"[X] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
