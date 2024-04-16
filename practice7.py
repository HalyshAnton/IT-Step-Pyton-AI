class Stack:
    def __init__(self):
        self.pages = []

    def push(self, page):
        self.pages.append(page)

    def pop(self):
        return self.pages.pop()

    def print(self):
        print(self.pages)

    def peek(self):
        return self.pages[-1]


history = Stack()

while True:
    action = input('Введіть дію(вихід, перейти на сторінку, повернутись назад, подивитись історію):')

    if action == 'вихід':
        break

    elif action == 'перейти на сторінку':
        page = input('Введіть сторінку: ')
        history.push(page)

    elif action == 'повернутись назад':
        page = history.pop()
        print(f'Ви покинули сторінку {page}')
        print(f'Ви повернулися на {history.peek()}')

    elif action == 'подивитись історію':
        history.print()
