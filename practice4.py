from queue import PriorityQueue


queue = PriorityQueue()

queue.put((1, "Mary"))
queue.put((3, "Sophy"))
queue.put((2, "John"))
queue.put((2, "Max"))
queue.put((2, "Julia"))

while not queue.empty():
    priority, client = queue.get()
    print(client, priority)
