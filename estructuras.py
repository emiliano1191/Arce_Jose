""" Consignas primera parte: Resolver cada enunciado utilizando las estructuras IF – ELSE – ELIF, según usted crea
correspondiente:
1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha
ganado el sorteo!
2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco,
seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!
3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
ingresado no es ninguno de esos, imprimir otro mensaje.
4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
“es vocal”. """



#  Enunciado 1:

numero = int(input("Ingrese un número: "))
if numero == 10:
    print("¡Usted ha ganado el sorteo!")


# Enunciado 2:

numero = int(input("Ingrese un número: "))
if numero == 10:
    print("¡Usted ha ganado el sorteo!")
elif numero < 10:
    print("¡Falto un poco, seguí participando!")
else:
    print("¡Te pasaste, a seguir intentando!")


# Enunciado 3:

dia_semana = input("Ingrese un día de la semana: ")
if dia_semana == "lunes":
    print("¡Es el comienzo de la semana!")
elif dia_semana == "viernes":
    print("¡Por fin es viernes!")
elif dia_semana == "sábado" or dia_semana == "domingo":
    print("¡Es un día de descanso!")
else:
    print("No reconocemos ese día.")


# Enunciado 4:

while True:
    caracter = input("Ingrese un caracter (0 para salir): ")
    if caracter == '0':
        break
    if len(caracter) == 1 and caracter.isalpha():
        if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
            print("VOCAL")
        else:
            print("NO VOCAL")
    else:
        print("Debe ingresar solo una letra.")


""" Ejercicios Estructuras Repetitivas:
Resolver cada enunciado utilizando las estructuras FOR – WHILE, según usted crea
correspondiente:

1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar
hasta que se ingrese -1.
2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
introducir). El programa debe informar de cuantos números introducidos son mayores que
0, menores que 0 e iguales a 0.
3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
contrario, el programa termina cuando se introduce un cero.
4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos.

 """



#  Enunciado 1:

suma = 0
numero = int(input("Ingrese un número (-1 para salir): "))
while numero != -1:
    suma += numero
    numero = int(input("Ingrese un número (-1 para salir): "))
print("La sumatoria de los números es:", suma)


#  Enunciado 2:

cantidad = int(input("Ingrese la cantidad de números a introducir: "))
mayores = 0
menores = 0
iguales = 0

for _ in range(cantidad):
    numero = float(input("Ingrese un número: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print("Cantidad de números mayores que 0:", mayores)
print("Cantidad de números menores que 0:", menores)
print("Cantidad de números iguales a 0:", iguales)


#  Enunciado 3:

while True:
    caracter = input("Ingrese un caracter (0 para salir): ")
    if caracter == '0':
        break
    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("VOCAL")
    else:
        print("NO VOCAL")


# Enunciado 4:

suma = 0
contador = 0

while True:
    numero = float(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print("La suma de los números es:", suma)
    print("La media de los números es:", media)
else:
    print("No se ingresaron números.")





