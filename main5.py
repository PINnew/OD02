class Stack:
    """Реализация стека с использованием списка"""
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Добавить элемент в стек"""
        self.stack.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент стека"""
        if self.is_empty():
            raise IndexError("Попытка удалить элемент из пустого стека")
        return self.stack.pop()

    def peek(self):
        """Посмотреть на верхний элемент стека без удаления"""
        if self.is_empty():
            raise IndexError("Попытка получить элемент из пустого стека")
        return self.stack[-1]

    def is_empty(self):
        """Проверить, пуст ли стек"""
        return len(self.stack) == 0

    def size(self):
        """Получить размер стека"""
        return len(self.stack)


class Queue:
    """Реализация очереди с использованием списка"""
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Добавить элемент в очередь"""
        self.queue.append(item)

    def dequeue(self):
        """Удалить и вернуть первый элемент очереди"""
        if self.is_empty():
            raise IndexError("Попытка удалить элемент из пустой очереди")
        return self.queue.pop(0)

    def peek(self):
        """Посмотреть на первый элемент очереди без удаления"""
        if self.is_empty():
            raise IndexError("Попытка получить элемент из пустой очереди")
        return self.queue[0]

    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return len(self.queue) == 0

    def size(self):
        """Получить размер очереди"""
        return len(self.queue)


class Graph:
    """Реализация графа"""
    def __init__(self):
        self.a = {}

    def add_vertex(self, vertex):
        if vertex not in self.a:
            self.a[vertex] = []

    def add_edge(self, v1, v2):
        if v1 not in self.a:
            self.add_vertex(v1)
        if v2 not in self.a:
            self.add_vertex(v2)
        self.a[v1].append(v2)
        self.a[v2].append(v1)

    def add_directed_edge(self, start, end):
        if start not in self.a:
            self.add_vertex(start)
        if end not in self.a:
            self.add_vertex(end)
        self.a[start].append(end)

    def display(self):
        for vertex, neighbors in self.a.items():
            print(f"{vertex}: {', '.join(map(str, neighbors))}")




# Использование стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Размер стека:", stack.size())            # Ожидается: 3
print("Верхний элемент стека:", stack.peek())  # Ожидается: 3
print("Удалённый элемент:", stack.pop())       # Ожидается: 3
print("Размер стека:", stack.size())           # Ожидается: 2
print()

# Использование очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Размер очереди:", queue.size())          # Ожидается: 3
print("Первый элемент очереди:", queue.peek()) # Ожидается: 1
print("Удалённый элемент:", queue.dequeue())  # Ожидается: 1
print("Размер очереди:", queue.size())        # Ожидается: 2
print()

# Использование графа
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_directed_edge("A", "C")
print("Граф:")
graph.display()