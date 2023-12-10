class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def __str__(self):
        return str(self.items)


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def new_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(task)

    def remove_task(self, priority):
        if priority in self.tasks and not self.tasks[priority].items:
            self.tasks.pop(priority)

    def __str__(self):
        result = ""
        for priority in sorted(self.tasks):
            tasks_with_same_priority = "; ".join(reversed(self.tasks[priority].items))
            result += f"{priority} — {tasks_with_same_priority}\n"
        return result.strip()


manager = TaskManager()

manager.new_task("спать", 4)
manager.new_task("играть", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("делать дз", 2)

print(manager)