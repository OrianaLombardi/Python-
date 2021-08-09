class Persona:
    def __init__(this,nombre, edad, *v, **d):    #*v (tupla)  **d (diccionario)
        this.nombre=nombre
        this.edad=edad
        this.valores=v
        this.diccionario=d
        
    def desplegar(this):                           #self y this es lo mismo
        print("Nombre: ", this.nombre)
        print("Edad: ", this.edad)
        print("Valores(tupla): ", this.valores)
        print("Diccionario: " , this.diccionario)
    
p1=Persona("Juan", 28)
p1.desplegar()
print()

p2=Persona("Karla", 30, 2,4,5)
p2.desplegar()
print()

p3=Persona("Paola", 33,4,9,m="manzana",p="pera", b="banana")
p3.desplegar()

