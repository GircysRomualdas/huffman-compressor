from node import Node

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

def sort_nodes(nodes):
    return sorted(nodes, key=lambda node: node.count)
