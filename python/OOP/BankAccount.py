#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
# Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False
def minimo (x):
    if len(x)==0:
        return False
    else:
        min = x[0]
        for y in range (0, len(x)):
            if x[y]<min:
                min = x[y]
        return min
x = minimo ([37,2,1, -9])
print(x)#output: -9