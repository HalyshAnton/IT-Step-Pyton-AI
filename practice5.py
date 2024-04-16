from queue import PriorityQueue


class TaskSolver:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_task(self, task, priority):
        self.queue.put((priority, task))

    def solve_next_task(self):
        if self.queue.empty():
            print("Всі завдання виконані")
            return

        priority, task = self.queue.get()

        print(f'Виконую {task}')


solver = TaskSolver()

solver.add_task('Завдання 2', 2)
solver.add_task('Завдання 3', 3)
solver.add_task('Завдання 1', 1)

solver.solve_next_task()
solver.solve_next_task()
solver.solve_next_task()