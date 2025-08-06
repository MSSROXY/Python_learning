# 1. Actualizar valores en diccionarios y listas:
# A continuación se presentan varias estructuras de datos.
# Realiza los siguientes cambios directamente:

matriz = [[10, 15, 20], [3, 7, 14]]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"],
}

coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]

# Realiza los siguientes cambios:

# Cambia el valor 3 en matriz por 6.
matriz[1][0] = 6
print(matriz)

# Cambia el nombre del primer cantante por "Enrique Martin Morales".
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

# En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".
ciudades["México"][2] = "Monterrey"
print(ciudades)

# En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
coordenadas[0]["latitud"] = "9.9355431"
print(coordenadas)


# 2. Recorrer una lista de diccionarios:  Utiliza estructuras de control para iterar la lista cantantes.
# Muestra el nombre y país de cada cantante.
# * BONUS: Presenta cada entrada con el siguiente formato: nombre - [Nombre del cantante], pais - [País]

for i, cantante in enumerate(cantantes):
    print(f"{i}. nombre - {cantante['nombre']}, país - {cantante['pais']}")


# 3. Obtener valores específicos desde una lista de diccionarios:
# Utilizando la lista cantantes, imprime por separado todos los valores correspondientes a la clave "nombre".
# Luego, imprime todos los valores correspondientes a la clave "pais".

nombre_cantantes = []
pais_cantantes = []
for cantante in cantantes:
    nombre_cantantes.append(cantante["nombre"])
    pais_cantantes.append(cantante["pais"])
print(nombre_cantantes, pais_cantantes)

# 4. Recorrer un diccionario con listas como valores:  Dado el siguiente diccionario:

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"],
}
# Realiza un recorrido del diccionario que imprima lo siguiente:
# La cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas.
# Cada elemento de la lista correspondiente, en líneas separadas.

for clave, lista in costa_rica.items():
    print(f"{len(lista)} - {clave.upper()}")
    for valor in lista:
        print(f"{valor}")
