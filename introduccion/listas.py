#se puede escribir como una lista de items separados por coma y corchetes
numeros = [1,2,3,4]
datos = [4,"una cadena",-15,3.14,"otra cadena"]

#para acceder a los elementos
print(datos[0])

#mostrar el ultimo elemento
print(datos[-1])

#utilizando slicing
print(datos[-2:])

#concatenar una lista con otra
numeros + [5,6,7,8]
print(numeros)

#reasignacion

pares = [0,2,4,5,8,10]
pares[3] = 6

#anador elementos al final de la lista
pares.append(12)
print(pares)

#asignacion con slicing
letras = ['a','b','c','d','e','f']
letras[:3]
letras[:3] = ['A','B','C']
print(letras)

#borrando los valores con slicing
letras[:3] = []
print(letras)

#otra forma de borrar
letras = []
print(letras)

#saber longitud de una lista
print(len(letras))

#listas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

r = [a,b,c]
print(r)

print(r[0])

#hacer referencias de las listas anidadas podemos hacer
#referencia de sus listas internas
print(r[0][0])
