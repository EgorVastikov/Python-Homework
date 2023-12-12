class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def get(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.data if current else None

    def remove(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                return
            current = current.next

        if current.next is None:
            return

        current.next = current.next.next

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' '.join(elements)



my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
