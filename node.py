
class Node:
    def __init__(self, count, ascii_code = None, left_node = None, right_node = None):
        self.left_node = left_node
        self.right_node = right_node
        self.ascii_code = ascii_code
        self.count = count
        self.code = None

    def __str__(self):
        return f"<{self.ascii_code}> <{self.count}>"
