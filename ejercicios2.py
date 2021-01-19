empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)
print(new_person)
print(type(new_person))
print(type(w))
print(len(new_person))
print("CLASS ACTIVITITES")

#CLASS PRACTICE JANUARY, 15, 2021
lista_pares = [2,4,6,8,0]
print(lista_pares) #output: [2,4,6,8,0]
#Todas comienzan en la posición 0
print(lista_pares[0]) #accedo a la posición 0 del arreglo. Output: 2

#ver el tamaño de una lista
print(len(lista_pares)) # output: 5 (cantidad de elementos)

#acceder al último elemento
print(lista_pares[len(lista_pares)-1])
print(lista_pares[-1]) #python me permite recorrer los elemento del arreglo con valores negativos
print(lista_pares[-2]) #output: 8
print(lista_pares[-5])#output: 2

#arreglo vacío
arreglo = []
print (len(arreglo)) #output: 0. De un arreglo vació EL TAMAÑO ES 0
print ("//////")

print()
#podemos hacer secciones de listas - dividir arreglos: #lista_pares = [2,4,6,8,0]
print(lista_pares[3:]) #output: [8,0], consideró el elemento de la posición 3
print(lista_pares[:3]) #output: [2, 4, 6] -> no considera el elemento en la posición 3
print(lista_pares[1:]) #output: [4, 6, 8, 0]
print(lista_pares[:4]) #output: [2, 4, 6, 8]
print(lista_pares[:]) #output: [2, 4, 6, 8, 0] #Todos los elementos

arreglo = lista_pares
print(arreglo)#[2, 4, 6, 8, 0]

#Modificar el valor de una lista
lista_pares[2]= 5 #el elemento en la posición 2 será igual a =
print(lista_pares) #output: [2, 4, 5, 8, 0]
print(arreglo) #output: [2, 4, 5, 8, 0] -> en js utilizabamos temp.

print ("//////")

#la variable llamada arreglo la igualamos. ambos elementos apuntan al mismo espacio de memoria
#y cuando modificamos un elemento automaticamente modifica arreglo
#la variable puedo modificarle las veces que quiera
arreglo2 = lista_pares[:]
print(arreglo2) #no recibió cambios, se obtienen los valores del arreglo;
# "arreglo = lista_pares" ahí se están igualando los valores, NO ES LO MISMO
#si modifico lista de pares, se modificaría arreglo, pero no arreglo2

#NOMBRE_ARREGLO = LISTA_NOMBRE[:] -> crear un arreglo temporal

arreglo.append("a") #agrega en la última posición
print(arreglo) #output: [2, 4, 5, 8, 0, 'a']

print("16 de enero 2021")

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])

for count in range(0,5):
    print("looping - ", count)

#while loop
y = 3
while y > 0:
    print(y)
    y = y - 1
else: #que quiero que haga si no se cumple la condición, cuando retorna falsa
    print("Final de sentencia else")

#for loop
for z in range (3,0,-1):
    print (z)










