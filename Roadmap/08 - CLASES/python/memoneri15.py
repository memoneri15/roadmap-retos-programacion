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
