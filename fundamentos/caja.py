class Caja:
    def __init__(self, alto, largo, ancho):
        self.alto=alto
        self.ancho=ancho
        self.largo=largo
        
    def volumen(self):
        return self.alto*self.ancho*self.largo
    
    
alto=int(input("Proporciona el alto: "))
largo=int(input("Proporciona el largo: "))
ancho=int(input("Proporciona el ancho: "))

caja=Caja(alto,largo,ancho)
print("El volumen de la caja es: " , caja.volumen() , "m3")