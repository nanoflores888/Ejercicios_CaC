class Cuenta():
    def __init__(self, titular='', cantidad=0, edad=0):
        self.__titular = titular
        self.__edad = edad
        self.__cantidad = cantidad
        
    def getTitular(self):
        return self.__titular
    
    def setTitular(self, titular):
        self.__titular = titular
        
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad = edad
        
    def getCantidad(self):
        return self.__cantidad
    
    def setCantidad(self, dinero):
        self.__cantidad = dinero
        
    def mostrar(self):
        print(f'Persona : {self.getTitular()}, Cantidad : {self.getCantidad()}, Edad : {self.getEdad()}')
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self, retiro):
            self.__cantidad = self.__cantidad - retiro

#Pruebas no parte del ejercicio.
if __name__ == "__main__": 
    p1 = Cuenta()
    p1.setTitular('Carlos')
    p1.setEdad(20)
    print(p1.mostrar())
    p1.ingresar(2000)
    print(p1.mostrar())
    p1.ingresar(2000)
    print(p1.mostrar())
    p1.retirar(500)
    print(p1.mostrar())
    p1.retirar(5000)
    print(p1.mostrar())