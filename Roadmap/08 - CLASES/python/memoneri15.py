"""
Ejercicio
"""


class Programmer:

    surname: str = none
  
    def __init__ (self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(
            f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}")


my_programmer = Programer("Brais", 36, ["Python", "Kotlin", "Swift"])
my_programmer.print()
my_programmer.surname = "Moure"
my_programmer.print()
my_programmer.edge = 37
my_programmer.print()

"""
Extra
"""

# LIFO


class Stack:

    def __init__(self):
        self.stack = []
  
    def push(self, item):
        self.stack.append(item)

    def pop:(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count:(self):
        return len(self.stack)

    def print:(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())


# FIFO


class Queue:
    
    def __init__ (self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)

    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
        
    def count:(self):
        return len(self.stack)
            
    def print:(self):
        for item in (self.stack):
            print(item)


my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
print(my_queue.count())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.deequeue())
print(my_queue.count())
