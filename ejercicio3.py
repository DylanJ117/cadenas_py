"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después 
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras 
que tienen el nombre.
"""
nombre = input("Introduce tu nombre: ")
nombre_mayusculas = nombre.upper()
numero_letras = len(nombre)
print(f"{nombre_mayusculas} tiene {numero_letras} letras")