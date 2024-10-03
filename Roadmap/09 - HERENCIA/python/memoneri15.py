"""
Ejercicio
"""


# Superclase

class Animal:

    def __init__ (self, name: str):
        self.name = name

    def sound():
        pass

# Subclases


class Dog(Animal):

    def sound():
        print("Guau!")

    
class Cat(Animal):
    
    def sound():
        print("Miau!")


def print_sound(animal: Animal):
    animal.soun()


my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Perro")
print_sound(my_dog)
my_cat = Cat("Gato")
print_sound(my_cat)

"""
Extra
"""


class Employee:
  
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employee = []

    def add(self, employee):
        self.employee.append(employee)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa.")


class ProjectManager(Employee):

    def coordinate_project(self):
        print(f"{self.name} esta coordinando su proyecto.")
  

class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} esta programando en {self.language}")

    def add(self, employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee} no se añadira.")



  
