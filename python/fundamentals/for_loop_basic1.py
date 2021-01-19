#1. Básico : imprime todos los enteros del 0 al 150.
for a in range (0,151,1):
    print(a)
#output: 0, 1, 2, 3... 150.

# 2. Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for b in range (5,1001,5):
    print(b)
#output: 5, 10, 15... 1000.

#3. Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar.
# Si es divisible por 10, imprima "Coding Dojo".

for value in range (1,101):
    if value %10 == 0:
        print("Coding")
        print ("Coding Dojo")
    elif value %5 == 0:
        print ("Coding")
    else:
    	print(value)

#4. ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
sum= 0
for i in range (0, 500000):
    if i%2 != 0:
        sum += i
print(sum)
#output: 62500000000

#5. Cuenta regresiva por cuatro : imprime números positivos a partir de 2018, cuenta atrás por cuatro.
for d in range (2018, 0, -4):
    print (d)
#output: 2018, 2014, 2010... 10, 6, 2.

# 6. Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum,
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3,
# el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 2
highNum = 9
mult = 3
for e in range (lowNum, highNum+1):
    if e % mult ==0:
        print(e)
#output: 3, 6, 9