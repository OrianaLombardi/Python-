#tupla mantiene el orden, pero no se puede modificar
frutas=("Naranja", "Platano", "Guayaba")
print(frutas)

#largo de la tupla
print(len(frutas))

#accediendo a un elemento
print(frutas[0])

#navegacion inversa
print(frutas[-1])

#rango
print(frutas[0:2]) #excluyendo el indice 2

#modificar un valor
frutasLista=list(frutas)
frutasLista[1]="Platanito"
frutas=tuple(frutasLista)
print(frutas)

#iterar una tupla
for fruta in frutas:
    print(fruta, end=" ")
    
#no podemos ni agregar ni eliminar elementos de una tupla

#eliminar por completo
del frutas
print(frutas)