import unittest
from node import Node
from encoding import (
    build_tree,
    build_encoding_map,
    serialize_tree,
    deserialize_tree,
    encode_text_to_bits,
    decode_bits_to_text
)

class TestEncoding(unittest.TestCase):
    def setUp(self):
        # Simple nodes for testing
        self.nodes = [
            Node(5, 'a'),
            Node(7, 'b'),
            Node(10, 'c'),
            Node(15, 'd'),
        ]

    def test_build_tree(self):
        sorted_nodes = sorted(self.nodes, key=lambda n: n.count)
        root = build_tree(sorted_nodes)
        self.assertIsInstance(root, Node)
        self.assertIsNone(root.character)  # root should be internal node, no character

    def test_build_encoding_map(self):
        sorted_nodes = sorted(self.nodes, key=lambda n: n.count)
        root = build_tree(sorted_nodes)
        encoding_map = build_encoding_map(root)
        self.assertIsInstance(encoding_map, dict)
        for char in ['a', 'b', 'c', 'd']:
            self.assertIn(char, encoding_map)
            self.assertRegex(encoding_map[char], '^[01]+$')

    def test_serialize_tree(self):
        sorted_nodes = sorted(self.nodes, key=lambda n: n.count)
        root = build_tree(sorted_nodes)
        serialized = serialize_tree(root)
        self.assertIsInstance(serialized, str)
        self.assertTrue(len(serialized) > 0)

    def test_deserialize_tree(self):
        sorted_nodes = sorted(self.nodes, key=lambda n: n.count)
        root = build_tree(sorted_nodes)
        serialized = serialize_tree(root)
        tokens = serialized.strip().split()
        deserialized_root = deserialize_tree(tokens)
        self.assertIsInstance(deserialized_root, Node)
        # Check some basic properties
        self.assertIsNone(deserialized_root.character)

    def test_encode_text_to_bits(self):
        text = "abcd"
        sorted_nodes = sorted([
            Node(text.count(c), c) for c in set(text)
        ], key=lambda n: n.count)
        root = build_tree(sorted_nodes)
        encoding_map = build_encoding_map(root)
        encoded_bits = encode_text_to_bits(text, encoding_map)
        self.assertIsInstance(encoded_bits, str)
        self.assertRegex(encoded_bits, '^[01]+$')
        self.assertTrue(len(encoded_bits) > 0)

    def test_decode_bits_to_text(self):
        text = "abcd"
        sorted_nodes = sorted([
            Node(text.count(c), c) for c in set(text)
        ], key=lambda n: n.count)
        root = build_tree(sorted_nodes)
        encoding_map = build_encoding_map(root)
        encoded_bits = encode_text_to_bits(text, encoding_map)
        decoded_text = decode_bits_to_text(encoded_bits, root)
        self.assertEqual(decoded_text, text)

if __name__ == "__main__":
    unittest.main()
