import unittest
from utils import get_character_frequencies, sort_nodes
from node import Node

class TestUtils(unittest.TestCase):
    def test_get_character_frequencies(self):
        text = "aabbbc"
        freq_nodes = get_character_frequencies(text)

        # Convert to dict {char: count} for easier testing
        result = {node.character: node.count for node in freq_nodes}
        expected = {'a': 2, 'b': 3, 'c': 1}
        self.assertEqual(result, expected)

    def test_sort_nodes(self):
        nodes = [
            Node(5, 'x'),
            Node(2, 'y'),
            Node(3, 'z')
        ]
        sorted_nodes = sort_nodes(nodes)
        sorted_counts = [node.count for node in sorted_nodes]
        expected_counts = [2, 3, 5]
        self.assertEqual(sorted_counts, expected_counts)

if __name__ == "__main__":
    unittest.main()
