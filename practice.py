class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

print(node1)
