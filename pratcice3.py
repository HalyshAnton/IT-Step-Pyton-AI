from queue import Queue


class BankQueue:
    def __init__(self):
        self.queue = Queue()

    def put_client(self, client):
        self.queue.put(client)

    def serve_next_client(self):
        if self.queue.empty():
            print("Не залишилось клієнтів у черзі")
            return

        client = self.queue.get()

        print(f'Ви обслуговуєте {client}')

    def number_clients(self):
        return self.queue.qsize()

    def is_empty_queue(self):
        return self.queue.empty()

    def print(self):
        temp_queue = Queue()

        while not self.queue.empty():
            client = self.queue.get()
            print(client, end=' <- ')
            temp_queue.put(client)

        print()

        self.queue = temp_queue


bank_queue = BankQueue()

bank_queue.put_client("Mary")
bank_queue.print()
bank_queue.put_client("Sophy")
bank_queue.print()

bank_queue.serve_next_client()
bank_queue.print()

bank_queue.put_client("Max")
bank_queue.print()

bank_queue.serve_next_client()
bank_queue.serve_next_client()
bank_queue.serve_next_client()