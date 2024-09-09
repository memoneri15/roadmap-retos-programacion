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

