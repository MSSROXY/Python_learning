import os
import shutil
from datetime import datetime
from pathlib import Path
ARCHIVO_INVENTARIO = "inventario.txt"

# Roxy Solano, David Ferrer, Tatu Vergara, Patricia Vidal, Gabriel Arriagada
def leer_inventario():
    if not os.path.exists(Path(__file__).parent/ARCHIVO_INVENTARIO):
        print("No existe el archivo inventario.")
        return
    with open(Path(__file__).parent/ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()
    if not contenido:
        print("El inventario está vacío.")
    else:
        print("\nInventario:")
        for linea in contenido:
            print(linea.strip())
def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = input("Precio (ej: 10 USD): ")
    cantidad = input("Cantidad (ej: 10 unidades): ")
    talla = input("Talla: ")

    with open(Path(__file__).parent/ARCHIVO_INVENTARIO, "a", encoding="utf-8") as archivo:
        archivo.write(f"\n{nombre}, {precio}, {cantidad}, {talla}")
    print("Producto agregado correctamente.")

def info_inv():
    if os.path.exists(Path(__file__).parent/ARCHIVO_INVENTARIO):
        tamaño = os.path.getsize(Path(__file__).parent/ARCHIVO_INVENTARIO)
        modificado = os.path.getmtime(Path(__file__).parent/ARCHIVO_INVENTARIO)
        fecha_mod = datetime.fromtimestamp(modificado).strftime("%d-%m-%Y %H:%M:%S")
        print(f"Tamaño: {tamaño} bytes , Ultima modificación: {fecha_mod}")
    else:
        print("El archivo no existe.")

def buscar_producto():
    busca = input("Ingrese nombre o palabra clave del producto: ").lower()
    with open(Path(__file__).parent/ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
        inv = archivo.readlines()

    coincidencias = [linea.strip() for linea in inv if busca in linea.lower()]
    if coincidencias:
        print("\n Producto(s) encontrado(s)")
        for i in coincidencias:
            print(i)
    else:
        print("No se encontró ningúna coincidencia.")

def eliminar_producto():
    ruta = Path(__file__).parent / ARCHIVO_INVENTARIO
    if not ruta.exists():
        print("No existe el archivo inventario.")
        return
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    if not lineas:
        print("El inventario está vacío.")
        return
    print("\nInventario actual:")
    for idx, linea in enumerate(lineas, start=1):
        print(f"[{idx}] {linea.strip()}")
    try:
        pos = int(input("Número de producto a eliminar: "))
        if not 1 <= pos <= len(lineas):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada no válida.")
        return

    # Copia de seguridad
    fecha = datetime.now().strftime("%d%m%Y_%H%M%S")
    copia_seguridad = Path(__file__).parent / f"copia_seguridad_{fecha}.txt"
    shutil.copy(ruta, copia_seguridad)
    print(f"Copia de seguridad creada: {copia_seguridad.name}")

    # Eliminar y guardar
    eliminado = lineas.pop(pos - 1).strip()
    with open(ruta, "w", encoding="utf-8") as f:
        f.writelines(lineas)

    print(f"Producto '{eliminado}' eliminado correctamente.")

def modificar_inventario():
    ruta = Path(__file__).parent / ARCHIVO_INVENTARIO
    if not ruta.exists():
        print("No existe el archivo inventario.")
        return
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    if not lineas:
        print("El inventario está vacío.")
        return

    print("\nInventario actual:")
    for idx, linea in enumerate(lineas, start=1):
        print(f"[{idx}] {linea.strip()}")

    try:
        pos = int(input("Número de producto a modificar: "))
        if not 1 <= pos <= len(lineas):
            print("Número inválido.")
            return
    except ValueError:
        print("Entrada no válida.")
        return

    nuevo = input("Ingresa la línea completa con los datos modificados: ").strip()
    if nuevo == "":
        print("No se realizaron cambios.")
        return

    # Reemplazar y guardar
    lineas[pos - 1] = nuevo + "\n"
    with open(ruta, "w", encoding="utf-8") as f:
        f.writelines(lineas)


def menu():
    opciones={
        '1':('Leer inventario', leer_inventario),
        '2':('Agregar producto', agregar_producto),
        '3':('Informacion de inventario', info_inv),
        '4':('Buscar producto', buscar_producto),
        '5':('Eliminar producto', eliminar_producto),
        '6': ('Modificar inventario', modificar_inventario),
        '7':('Salir', exit)
    }
    while True:
        print('||| Menu Inventario|||')
        for key, (opcion, _) in opciones.items():
            print(f'[{key}] {opcion}')
        seleccion=input('opcion: ')
        if seleccion in opciones:
            opciones[seleccion][1]()
        else:
            print('opcion invalida intente denuevo')

menu()


