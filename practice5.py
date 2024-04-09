class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next is not None:
            tail = tail.next

        tail.next = new_node
        new_node.prev = tail


my_list = DoubleLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print()
