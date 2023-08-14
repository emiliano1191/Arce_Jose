import random

list_nombres_familiares = ['Arturo','Amalia','Antonella','Amanda', 'Marta Abuela','Torrico Abuelo']

temperaturas_agosto = [28.5, 29.0, 30.2, 31.1, 28.8, 27.4, 26.7, 29.5, 30.7, 31.9, 29.8, 28.3, 27.6, 26.9, 28.4, 30.0, 31.2, 30.8, 29.7, 28.1, 26.5, 25.8, 27.3, 29.6, 31.5, 30.3, 29.2, 28.7, 27.9, 26.2, 25.4]

Ciudades_visitadas = ['Alta Gracia','Calamuchita','Río Cuarto','villa maría', 'Roma', 'Torres','Río de Janeiro']

eventos_importantes = [
    ["1991-04-11", "Nacimiento"],
    ["1996-09-01", "Comienzo de la Escuela"],
    ["2009-06-15", "Finalización de la Escuela Secundaria"],
    ["2010-11-01", "Comienzo de la Universidad"],
    ["2016-06-15", "nunca sucedio"],
    ["2010-01-01", "Comienzo de la Carrera Profesional"],
    ["2018-06-01", "Primer Viaje Internacional"],
    ["2020-03-15", "Cursos en Backend"],
    ["2023-08-13", "comienzdo de estudios en ISPC"]
]

temperaturas_agosto.sort()
print(temperaturas_agosto)
print(list_nombres_familiares)
print(eventos_importantes)

temperaturas_septiembre = [28.0, 27.5, 26.8, 25.6, 24.9, 25.7, 26.4, 27.2, 28.1, 29.0, 30.2, 29.8, 28.5, 27.3, 26.9]
temperaturas_agosto.extend(temperaturas_septiembre)

list_nombres_familiares.remove("Marta Abuela")
list_nombres_familiares.remove("Torrico Abuelo")
print(list_nombres_familiares)
print(temperaturas_agosto)

Ciudades_visitadas.remove('Roma')
print(Ciudades_visitadas)


# Crear tres tuplas con datos aleatorios
tupla_1 = (random.randint(1, 100), random.uniform(0.0, 1.0), random.choice(['rojo', 'verde', 'azul', 'amarillo','naranja','negro']))
tupla_2 = (random.randint(1, 100), random.uniform(0.0, 1.0), random.choice(['rojo', 'verde', 'azul', 'amarillo','naranja','negro']))
tupla_3 = (random.randint(1, 100), random.uniform(0.0, 1.0), random.choice(['rojo', 'verde', 'azul', 'amarillo','naranja','negro']))
tupla_4 = (random.randint(1, 100), random.uniform(0.0, 1.0), random.choice(['rojo', 'verde', 'azul', 'amarillo','naranja','negro']))
# Crear una lista que contenga las tres tuplas
lista_de_tuplas = [tupla_1, tupla_2, tupla_3, tupla_4]

# Mostrar la lista de tuplas
print(lista_de_tuplas)

# CREAMOS un Diccionario
datos_nucleo_familiar = {
    "12345678": "Arturo",
    "23456789": "Amanda",
    "34567890": "Amalia",
    "35579867": "yo"
}

# Agregar datos de familia ampliada
datos_nucleo_familiar["45678901"] = "Ana"  # Hermana
datos_nucleo_familiar["56789012"] = "Torrico"  # Abuelo
datos_nucleo_familiar["67890123"] = "Marta"  # Abuela
datos_nucleo_familiar["78901234"] = "Carlos"  # Cuñado

""" print(datos_nucleo_familiar) """

print("Diccionario de Datos Familiares:")
for dni, nombre in datos_nucleo_familiar.items():
    print(f"DNI: {dni}, Nombre: {nombre}")

import random
import string

def generar_clave():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

nuevo_diccionario = {}



import random
import string



def generar_numero_telefono():
    numero = ''.join(random.choices(string.digits, k=8))
    return f'11-{numero[:4]}-{numero[4:]}'

diccionario_numeros_telefono = {}

# Generar claves autogeneradas y valores de números de teléfono
for _ in range(5):
    clave = ''.join(random.choices(string.ascii_uppercase, k=3))
    numero = generar_numero_telefono()
    diccionario_numeros_telefono[clave] = numero

# Mostrar el diccionario con las claves y los números de teléfono
print("Diccionario de Números de Teléfono:")
for clave, numero in diccionario_numeros_telefono.items():
    print(f"Clave: {clave}, Número de Teléfono: {numero}")
