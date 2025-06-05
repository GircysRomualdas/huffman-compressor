from node import Node, build_tree, sort_nodes

from temp import *

def main():
    data_str = test_data
    nodes = []

    for char in data_str:
        ascii_code = ord(char)
        found = False

        for node in nodes:
            if node.ascii_code == ascii_code:
                node.count += 1
                found = True
                break

        if not found:
            nodes.append(Node(1, ascii_code))

    sorted_nodes = sort_nodes(nodes)
    root_node = build_tree(sorted_nodes)

    print_tree_pretty(root_node)
    print(f"len: {len(test_data)}")

if __name__ == "__main__":
    main()
