#1 Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

"""
def division (a,b):
    return a/b

try:
    resultado = division (int(input(f"Introduce un primer numero: ")), int(input ("Introduce un segundo numero: ")))
    print ("No ocurrieron errores")
except Exception as e:
    print (f"Ocurrio un error. {e}")
else:
    print (f"El resultado final es {resultado}")

"""
#2 Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

"""
def suma (a,b):
    return a + b

try:
    resultado = suma (int(input(f"Introduce un primer numero: ")), (input ("Introduce un segundo numero: ")))
    print ("No ocurrieron errores")
except Exception as e:
    print (f"Ocurrio un error. {e}")
else:
    print (f"El resultado final es {resultado}")

"""

#3 Escribe un programa que intente acceder a una clave que no existe en un
# diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

"""
diccionario = {"nombre": "Juant",
               "Apellido": "Soler",
               "Edad": 23}

try:
    print (diccionario["Direccion"])
except KeyError as e:
    print (f"Error {e}, esa key no se encuentra")

"""

#4 Esncrmensaje de error al usuario. ibe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
#embargo, también intenta crear el archivo si no existe.

"""
try:
    larchivo = open("archivo.txt", "r", encoding="utf-8")
except Exception as e:
    print (f"El archivo no existe {e}, se creara uno")
    larchivo = open("archivo.txt", "w", encoding="utf-8" )
    larchivo.write ("Este archivo contiene texto")
else:
    larchivo = open("archivo.txt", "r", encoding="utf-8")
    contenido = larchivo.read()
    print (contenido)
    larchivo.close()

"""

#5 Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
#captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario

def division (a,b):
    return a + b

try:
    resultado = division (int(input(f"Introduce un primer numero: ")), int(input ("Introduce un segundo numero: ")))
    print ("No ocurrieron errores")
except Exception as e:
    print (f"Ocurrio un error. {e}")
else:
    print (f"El resultado final es {resultado}")