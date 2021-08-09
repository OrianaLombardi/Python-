class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
        
    def get_nombre(self):
        return self.__nombre 
        
    def set_nombre(self,nombre):
        self.__nombre=nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self,edad):
        self.__edad=edad
                                     
        
#GET PARA LEER INFO DEL ATRIBUTO 
#SET PARA MODIFICAR EL VALOR DEL ATRIBUTO PRIVADO
#__ ADELANTE LO VUELVE PRIVADO

        
p1=Persona("Juan",18)
#print(p1.__nombre) #marca error
print(p1.get_nombre())
print(p1.get_edad())

#p1.__nombre="Karla" error
p1.set_nombre("Karla")
p1.set_edad(20)
print(p1.get_nombre())
print(p1.get_edad())
