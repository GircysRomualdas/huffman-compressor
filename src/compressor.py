from .encoding import (
    build_encoding_map,
    build_tree,
    decode_bits_to_text,
    deserialize_tree,
    encode_text_to_bits,
    serialize_tree,
)
from .file_io import (
    read_compressed_file,
    read_text_file,
    write_compressed_file,
    write_text_file,
)
from .utils import get_character_frequencies, sort_nodes


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
    output_path = f"{path}.huff.bin"
    write_compressed_file(serialized_tree, encoded_bitstring, output_path)

    original_size = len(text_data.encode("utf-8"))
    compressed_size = len(encoded_bitstring) // 8
    return output_path, original_size, compressed_size


def decompress_file(path):
    serialized_tree, bitstring = read_compressed_file(path)
    root_node = deserialize_tree(serialized_tree.strip().split())
    decoded_text = decode_bits_to_text(bitstring, root_node)
    output_path = f"{path.removesuffix('.huff.bin')}.huff"
    write_text_file(output_path, decoded_text)
    return output_path
