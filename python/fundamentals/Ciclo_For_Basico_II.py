#1.
# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

#creando un arreglo vacío
def biggie_size (x):
    biggie_size2 = []
    for y in range(0, len(x)):
        if x [y] > 0:
            biggie_size2.append("big")
        else:
            biggie_size2.append(x[y])
    return biggie_size2
x = biggie_size([- 1, 3, 5, -5])
print(x) #si hubiera un número 0 se mantiene, no cambia a big
#output: [-1, 'big', 'big', -5]

#sin un arreglo vacío
def biggie_size (x):
    for y in range(0, len(x)):
        if x [y] > 0:
        	x[y]="big"
        else:
        	x[y] = x[y]
    return x
x = biggie_size([- 1, 3, 5, -5])
print(x) #si hubiera un número 0 se mantiene, no cambia a big
#output: [-1, 'big', 'big', -5]

#2.
#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def count_positives (x):
    sum = 0
    for y in range(0, len(x)):
        if x[y] > 0:
            sum = sum + 1
    x.pop()
    x.append(sum)
    return x
x = count_positives ([1,6,-4,-2,-7,-2])
print(x) #output: [1,6,-4,-2,-7,2]

#3.
#Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sum_total (arreglo):
    total = 0
    for elementos in arreglo :
        total +=elementos
    return total
arreglo = sum_total([1,2,3,4])
print (arreglo) #output: 10
arreglo = sum_total([6,3,-2])
print(arreglo) #output: 7

#4.
#Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def average (arreglo):
    total = 0
    for elementos in arreglo :
        total +=elementos
    return total/len(arreglo)
arreglo = average([1,2,3,4])
print (arreglo)
#output: 2.5

#5.
#Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0
def long(x):
    return len(x)
x = long([37,2,1, -9])
print(x) #output: 4

#6.
#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False
def minimo (x):
    if len(x)==0:
        return False
    else:
        min = 0
        for y in range (0, len(x)):
            if x[y]<min:
                min = x[y]
        return min
x = minimo ([37,2,1, -9])
print(x)#output: -9

#7.
#Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía,
# haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False
def maximo (x):
    if len(x)==0:
        return False
    else:
        max = 0
        for y in range (0, len(x)):
            if x[y]>max:
                max = x[y]
        return max
x = maximo ([37,2,1, -9])
print(x)#output: 37

#8.
#Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total,
# promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9,
# 'máximo': 37, 'longitud': 4}

def ultimate_analysis (x):
    max = 0
    min = 0
    sum = 0
    for y in range (0, len(x)):
        if x[y]>max:
            max = x[y]
        if x[y]<min:
        	min = x[y]
        sum = sum + x[y]
        promedio = sum/len(x)
    ultimate_analysisdict = {"total": sum, "promedio": promedio, "minimo": min, "maximo": max, "longitud": len(x) }
    return ultimate_analysisdict
x = ultimate_analysis ([37,2,1, -9])
print(x)

#9.
#Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos.
#Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

#9A
def reverse_list (list):
    list.reverse()
    return list
list = reverse_list([37,2,1, -9])
print (list)

#9B
list2 = [37,2,1, -9]
invertidos = list2[::-1]
print(invertidos)