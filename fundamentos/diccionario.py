#un diccionario esta compuesto de llave, valor(key,value)

diccionario={
    "IDE":"Integrated development environment",
    "OOP": "Object oriented programming",
    "DBMS": "Database management system"
    
}
print(diccionario)

#largo
print(len(diccionario))

#accediendo a un elemento
print(diccionario["IDE"])

#OTRA FORMA DE ACCEDER
print(diccionario.get("IDE"))

#modificando valores
diccionario["IDE"]="Integrated DEVELOPMENT ENVIROMENT"
print(diccionario)

#for termino in diccionario:
 #   print(termino)
    
for termino in diccionario:
    print(diccionario[termino])
    
#for valor in diccionario.values():
 #   print(valor)
    
#comprobando existencia del elemento
print("IDE" in diccionario)


#agregar nuevos elementos
diccionario["PK"]="Primary key"
print(diccionario)

#remover elementos
diccionario.pop("DBMS")
print(diccionario)

#limpiar/eliminar
diccionario.clear()
print(diccionario)

#eliminar por completo
del diccionario
print(diccionario)