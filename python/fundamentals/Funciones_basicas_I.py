#1
def a():
    return 5
print(a())
#output: 5

#2
def a():
    return 5
print(a()+a()) #5+5=10
#output: 10

#3
def a():
    return 5 #retorna esto, y hasta ahí llega la función
    return 10
print(a())
#output: 5

#4
def a():
    return 5
    print(10) #no se imprime esto, la función terminó con el return
print(a())
#output: 5

#5
def a():
    print(5) #output: 5
x = a() #se le asigna a x el valor de a, pero a() no tiene ningun valor asignado
print(x) #indefinido
#output: 5, none

#6
def a(b,c):
    print(b + c)
print(a(1,2) + a(2,3))
#output: TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
#se produce el error porque la función no retorna nada, si tuviera "return b + c" el output sería; 3, 5, 8

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#output: 25

#8
def a():
    b = 100
    print(b) #100
    if b < 10:
        return 5
    else:
        return 10 #100 no es menor a 10, por lo tanto retorna 10
    return 7
print(a()) #10
#output: 100, 10

#9
def a(b,c):
    if b<c: #2<3=true, 5<3=false,
        return 7
    else:
        return 14
    return 3
print(a(2,3)) #7
print(a(5,3)) #14
print(a(2,3) + a(5,3)) #7+14=21
#output: 7, 14, 21

#10
def a(b,c):
    return b+c #8
    return 10
print(a(3,5))
#output: 8

#11
b = 500
print(b) #500 - 1
def a():
    b = 300
    print(b) #300 - 3
print(b) #500 - 2
a() #entramos a la función, print b =300, pero no retorna nada (3)
print(b) #500 -4
#output: 500, 500, 300, 500

#12
b = 500
print(b) #1. 500
def a():
    b = 300
    print(b) #3. 300
    return b #retorna el valor de b=300
print(b) #2. valor de b = 300, aun no se ha hecho el llamado a la función
a()
print(b) #4. 300
#output: 500, 500, 300, 300

#13
b = 500
print(b) #1. 500
def a():
    b = 300
    print(b) #3. 300
    return b
print(b) #2. 500
b=a() #b = 300
print(b)#4. 300
#output: 500, 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#output: 1, 3, 2
#al ejecutar la función imprime 1, luego hace el llamado a la función b e imprime 3, luego sigue su ciclo normal
#e imprime 2

#15
def a():
    print(1)
    x = b()
    print(x) #5
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#output: 1, 3, 5, 10