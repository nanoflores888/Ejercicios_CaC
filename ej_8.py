from ej_7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular='', cantidad=0, edad=0, bono=0):
        super().__init__(titular, cantidad, edad)
        self.__bono = bono
        
    def getBono(self):
        return self.__bono
    
    def setBono(self, bono):
        self.__bono = bono
        
    def es_titular_valido(self):
        return self.getEdad() < 25 and self.getEdad() >= 18
    
    def retirar(self, retiro):
        if self.es_titular_valido() == False:
            print(f'La cuenta de {self.getTitular()} no es valida para el retiro de dinero.')
        elif self.es_titular_valido() == True:
            return super().retirar(retiro)
        
    def mostrar(self):
        if self.es_titular_valido() == False:
            print(f'NO ES UNA CUENTA JOVEN, Persona : {self.getTitular()}, Cantidad : {self.getCantidad()}, Edad : {self.getEdad()}, Bono : {self.getBono()}%')
        elif self.es_titular_valido() == True:
            print(f'CUENTA JOVEN, Persona : {self.getTitular()}, Cantidad : {self.getCantidad()}, Edad : {self.getEdad()}, Bono : {self.getBono()}%')

        

#Pruebas no parte del ejercicio

#Test 1
p2 = CuentaJoven()
p2.setTitular('Pepito')
p2.setCantidad(2000)
p2.setEdad(28)
p2.ingresar(1000)
p2.retirar(2500) #No es posible por la edad
print(p2.mostrar())

#Test 2
p3 = CuentaJoven()
p3.setTitular('Juan')
p3.setCantidad(5000)
p3.setEdad(20)
p3.setBono(25)
p3.ingresar(1000)
p3.retirar(1000)
print(p3.mostrar())