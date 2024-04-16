class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        '''
        Добавляє елемент в чергу
        :param data:
        :return: None
        '''

        node = Node(data)

        if self.is_empty():
            self.head = self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        """
        Повертає перший елемент
        :return: data
        """

        if self.is_empty():
            raise IndexError('Черга пуста')

        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return data

    def is_empty(self):
        return self.head is None


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())


