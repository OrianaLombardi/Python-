class Aritmetica:
    """Clase aritmetica para realizar las operaciones de suma"""
    def __init__(self, operando1, operando2):
        self.operando1=operando1
        self.operando2=operando2
        
    """Se realiza la operacion con los atributos de la clase"""
    def sumar(self):
        return self.operando1+self.operando2
   
    def restar(self):
        return self.operando1-self.operando2
    
    def division(self):
        return self.operando1/self.operando2
    
    def multiplicacion(self):
        return self.operando1*self.operando2


#creamos un nuevo objeto

resultado=Aritmetica(15,60)
print("Resultado suma: ", resultado.sumar())
print("Resultado resta: ", resultado.restar())
print("Resulado division: ", resultado.division())
print("Resultado multiplicacion: " , resultado.multiplicacion())


