# 1. TAREA: imprimir "Hola mundo"
print("Hola Mundo")

# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print("Hola",name)	# con una coma
print("Hola "+name)	# con un +

# 3. imprimir "Hola 42!" con un numero en una variable
name = "42"
print("Hola", name)	# con una coma
print("Hola "+name)	# con un + - !Este debería darnos un error!
# error si la variable name = 42, se puede solo concatenar str, no int.
#NinjaBonus: se puede resolver el error desde arriba sin cambiar el signo + por una coma (,) cambiando el tipo de
# variable de int a str (colocancole comillas al valor de la variable)

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} y {}.".format(fave_food1, fave_food2)) # con .format()
print(f"Me encanta comer {fave_food1} y {fave_food2}.") # con una cadena f

#¡Dedica unos minutos a jugar con otros métodos de cuerda para ver qué hay ahí fuera!
print(fave_food1.upper())
print(fave_food2.title())
print("Adoro comer " + fave_food1.lower()+ " y " + fave_food2.lower())
