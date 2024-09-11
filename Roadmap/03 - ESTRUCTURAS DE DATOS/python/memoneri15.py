"""
Extra
"""

# Listas
my_list = ["Brais", "Bl4ck", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor") # Insercion
my_list.append("Castor")
print(my_list)
my_list.remove("Brais") # Eliminacion
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "Cuervillo" #Actualizacion
print(my_list)
my_list.sort() #Ordenacion
print(my_list)
print(type(my_list))

# Tuplas
my_tuple = ("Brais", "Moure", "@moredev", "36")
print(my_tuple[1]) # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print(type(my_tuple))

# Sets
my_set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
my_set.add("memoneri15@hotmail.com") # Inserción
my_set.add("memoneri15@hotmail.com")
print(my_set)
my_set.remove("Moure") # Eliminación
print(my_set)
my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {
  "name":"Brais",
  "surname":"Moure",
  "alias":"@mouredev",
  "age":"36"
}
my_dict.["email"] = "memoneri15@hotmail.com" # Inserccion
print(my_dict)
del my_dict["surname"] # Eliminacion
print(my_dict)
print(my_dict["name"]) # Acceso
my_dict["age"] = "37" # Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

"""
Extra
"""


def my_agenda():

  agenda = {}

  def insert_contact():
       phone = input("Introduce el teléfono del contacto: ")
          if phone.isdigit() and len(phone)  > 0 and len(phone) <= 11: 
              agenda[name] = phone
          else:
              print(
                  "Debes introducir un número de teléfono con un máximo de 11 dígitos.")
            
  while True:
  
  print("")
  print("1. Buscar contacto")
  print("2. Insertar contacto")
  print("3. Actualizar contacto")
  print("4. Eliminiar contacto")
  print("5. Salir")

  option = input("\nSelecciona una opción: ")

  match option:
      case "1":
          name = input("Introduce el nombre del contacto a buscar: ")
          if name in agenda:
              print(
                  f"el número de télefono de {name} es {agenda[name]}.")
          else:
              print(f"El contacto {name} no existe.")
      case "2":
          name = input("Introduce el nombre del contacto: ")
          insert_contact() 
      case "3":
          name = input("Introduce el nombre del contacto a actualizar: ")
          if name in agenda
             insert_contact()
          else:
              print(f"El contacto {name} no existe. ")        
      case "4":
          name = input("Introduce el nombre del contacto a eliminar: ")
          if name in agenda: 
              del agenda[name]
          else:
              print(f"El contacto {name} no existe. ")
         case "5":
          print("Saliendo de la agenda.")
          break
      case _:
          print("Opción no válida. Elige una opción del 1 al 5.")


my_agenda()
