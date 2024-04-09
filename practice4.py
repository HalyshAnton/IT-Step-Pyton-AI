# Клас Node - представляє вузол списку з певними даними та посиланням на наступний (і попередній у двосв'язному) вузол
class Node:
    def __init__(self, data):
        self.data = data  # Зберігаємо дані у вузлі
        self.next = None  # Посилання на наступний вузол у списку
        self.prev = None  # Посилання на попередній вузол у двосв'язному списку


# Клас для черги реєстрації пасажирів
class RegistrationQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next


# Клас для черги посадки пасажирів
class BoardingQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def move_forward(self, data):
        # Знайти node з потрібним data
        node = self.head

        while node is not None and node.data != data:
            node = node.next

        # Якщо потрібного вузла немає
        if node is None:
            print('Немає пасажира в черзі')
            return

        # Якщо пасажир в кінці черги
        if node.next is None:
            print('Пасажир в кінці черги')
            return

        # Якщо node не в голові, а node.next не в хвості
        if node.prev and node.next.next:
            red = node.prev
            green = node
            blue = node.next
            black = node.next.next # blue.next
            # змінюємо посилання вперед
            red.next, green.next, blue.next = blue, black, green
            # змінюємо посилання назад
            green.prev, blue.prev, black.prev = blue, red, green

        # Якщо node в голові, а node.next не в хвості
        elif node.next.next:
            red = node.prev # None, немає next
            green = node
            blue = node.next
            black = node.next.next

            # змінюємо посилання вперед
            green.next, blue.next = black, green # без red.next
            # змінюємо посилання назад
            green.prev, blue.prev, black.prev = blue, red, green

            # тепер blue в голові
            self.head = blue

        # Якщо node не в голові, а node.next в хвості
        elif node.prev:
            red = node.prev
            green = node
            blue = node.next
            black = node.next.next # None, немає prev

            # змінюємо посилання вперед
            red.next, green.next, blue.next = blue, black, green
            # змінюємо посилання назад
            green.prev, blue.prev = blue, red # без black.prev

            # тепер green в хвості
            self.tail = green

        # Якщо node голові і node.next в хвості
        else:
            red = node.prev # None, немає next
            green = node
            blue = node.next
            black = node.next.next # None, немає prev

            # змінюємо посилання вперед
            green.next, blue.next = black, green # без red.next
            # змінюємо посилання назад
            green.prev, blue.prev = blue, red, green # без black.prev

            # тепер blue в голові, а green в хвості
            self.head = blue
            self.tail = green

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end=' -> ')
            node = node.next

        print()


my_list = BoardingQueue()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print()
print()

print('3 вперед')
my_list.move_forward(3)
my_list.print()
print()

print('5 вперед')
my_list.move_forward(5)
my_list.print()
print()

print('3 вперед')
my_list.move_forward(3)
my_list.print()
print()

print('1 вперед')
my_list.move_forward(1)
my_list.print()
print()

