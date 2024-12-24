# структура данных Стек (Stack)
class Stack:
   def __init__(self):
       self.items = []

# is_empty — проверка, пустой ли стек
   def is_empty(self):
       return self.items == []

# push — добавление элемента в стек
   def push(self, item):
       self.items.append(item)

# pop — удаление верхнего элемента
   def pop(self):
       return self.items.pop()

# peek — получение верхнего элемента без удаления
   def peek(self):
       return self.items[-1]


stack = Stack()

print(stack.is_empty()) # проверка stack он пустой значит True

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty()) # проверка stack он пустой значит False

print(stack.peek()) # проверка последнего stack 3
