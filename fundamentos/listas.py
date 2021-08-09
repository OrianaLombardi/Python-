nombres=["Juan", "Karla", "Ricardo", "Maria"]
print(nombres)

#Conocer el largo de la lista
print(len(nombres))

#el elemento 0
print(nombres[0])

#navegacion inversa
print(nombres[-1])
print(nombres[-2])

#Imprimir rango
print(nombres[0:2]) #sin incluir el indice 2

#Imrpimir los elementos de inicio hasta el indici proporcionado
print(nombres[:3])#sin incluir el indice 3

#imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:])

#cambiar los elementos de una lista
nombres[3]="Ivone"
print(nombres)

#iterar la lista
for nombre in nombres:
    print(nombre)
    
#revisar si existe un elemtno en la lista
if "Carla" in nombres:
    print("Karla si existe en la lista")
else:
    print("El elemento buscado no existe en la lista")
    
#agregar un nuevo elemento
nombres.append("Lorenzo")
print(nombres)

#insertar un nuevo elemento en el indice proporcionado
nombres.insert(1,"Octavio")
print(nombres)

#remover un elemento
nombres.remove("Octavio")
print(nombres)

#remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)

#remover el indice indicado de la lista
del nombres[0]
print(nombres)

#limpiar los elementos de nuestra lista
nombres.clear()
print(nombres)

#eliminar nuestra lista
del nombres
print(nombres)