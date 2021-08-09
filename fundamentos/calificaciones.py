numero=int(input("Proporciona un numero entre 0-10: "))
calificacion:None

if numero>=9 and numero<=10:
    calificacion="A"
elif numero>=8 and numero<9:
    calificacion="B"
elif numero>=7 and numero<8:
    calificacion="C"
elif numero>=6 and numero<7:
    calificacion="D"
elif numero>=0 and numero<6:
    calificacion="F"
else:
    calificacion="Valor desconocido "
    
print("La nota del alumno es: ", calificacion)
    
    