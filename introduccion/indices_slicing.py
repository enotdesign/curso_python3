palabra = "python"

#+---+---+---+---+---+---+
#| P | Y | T | H | O | N |
#+---+---+---+---+---+---+
#  0   1   2   3   4   5

#escogiendo letras con el indice

#caracter en la posicion 0 = P
print(palabra[0])
#caracter en la posicion 3 T
print(palabra[3])

#buscando caracteres en negativo
#se obtiene el ultimo caracter
print(palabra[-1])


#SLISING
#nos muestra las letras selecionadas, el final se excluye
print(palabra[0:2])

#desde el dos hasta el utilmo caracer
print(palabra[2:-1])
print(palabra[2:])

#muestras la palabra completa
print(palabra[:])