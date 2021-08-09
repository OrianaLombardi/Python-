#a= int(input("Proporciona un valor:"))
a=3
valorMinimo=0
valorMaximo=5
dentroRango= (a>=valorMinimo  and a<=valorMaximo)

#print(dentroRango)

if(dentroRango):
    print("Estamos dentro del rango ")
    
else:
    print("No estamos dentro del rango")
    
    
vacaciones= False
diaDescanso=False

if(vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")
    
    
#if(not(vacaciones or diaDescanso)):
#    print("Puedes ir al parque")
#else:
 #   print("Tienes deberes que hacer")
    
#print(not(vacaciones))