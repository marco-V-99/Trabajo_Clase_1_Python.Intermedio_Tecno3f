#1 Calcular el mayor de dos números ingresados por teclado usando un operador ternario
def mayor():
    try:
        a = int(input("introduce el primer valor: "))
        b = int(input("introduce el segundo balor: "))
    except ValueError:
        print (f"Eso no es un numero")
    else:
        mayor = print(f"a: ({a}) es mayor a b: ({b})" if a > b else f"b:({b}) es mayor que a:({a})") 

mayor()

#2 Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

def find_word(f_arg,*argv):
    entrada = input ("¿Que palabra queres buscar?")
    for arg in argv:
        print (f"Se encontro la palabra: {entrada}" if entrada == arg else "no se encontro la palabra")

find_word("python", "foo", "bar", "hola", "perro", "sandia", "fighters")

#3 Determinar si un número es par o impar
def num_par():
    a = int(input("Introduzca un numero: "))
    print(f"El numero es par" if a % 2 == 0 else "El numero es inpar")

num_par()

#4 Calcular el promedio de una lista de números usando args y un operador ternario

    
#5 Imprimir un mensaje de error si no se pasan suficientes argumentos


