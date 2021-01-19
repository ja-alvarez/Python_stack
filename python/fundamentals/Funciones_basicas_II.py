#1. Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia
# atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

def cuenta_regresiva (n):
    cuenta = []
    for a in range (n, 0-1, -1):
       cuenta.append(a)
    return cuenta
cuenta = cuenta_regresiva(5)
print(cuenta)

#2. Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el
# segundo. Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

lista = [1,2]
def print_and_return():
    print (lista[0])
    return lista[1]
print_and_return()

#3. First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la
# longitud de la lista. Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

lista2 = [1,2,3,4,5]
def first_plus_length ():
    return lista2[0]+len(lista2)
y = first_plus_length()
print(y)

#4.Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo
# los valores de la lista original que sean mayores que su segundo valor.
# Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la
# función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False

nuevalista = []
def values_greater_than_second (x):
    for y in range(0, len(x)):
        if x[y] > x[1]:
            nuevalista.append(x[y])
    if len(nuevalista) > 2:
        print(len(nuevalista))
        print(nuevalista)
    else:
        return False
x = values_greater_than_second([5,2,3,2,1,4])


#5. Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función
# debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]

def length_and_value (a,b):
    arreglo = []
    for x in range (0,a):
        arreglo.append(b)
    return arreglo
x = length_and_value(4, 7)
print (x)


