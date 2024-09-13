"""
Operaciones
"""
s1 = "Hola"
s2 = "Pythonthon"

# Concatenacion
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print([:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas, minúsculas y letras en mayúscula
print(s1.upper())
print(s1.lower())
print("brais moure".title())
print("brais moure".capitalize())

# Eliminación de espacios al principio y al final
print(" brais moure ".strip())

# Búsqueda al principio y al final
print(s1.startwith("Ho"))
print(s1.startwith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Brais Moure @mouredev"

# Búsqueda de posición
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find(M))
print(s3.lower().find("m"))

# Búsqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Tranformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones númericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


"""
Extra
"""


def check(word1: str, word2: str):

    # Palíndromo
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagrama
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted.(word2)}")

    # Isograma
     

check("radar", "python")
check("amor", "roma")
