class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self, cantidad):
        self.__saldo += cantidad
        return "Tu saldo ahora es de ", self.__saldo
    
    def retirar(self, cantidad):
        if (self.__saldo == 0) or (self.__saldo < cantidad):
            return "Insuficientes fondos"
        else:
            self.__saldo -= cantidad
            return "Toma tu dinero ", cantidad

#---------------------------------------Iniciating programing
cuentaDeBBVA = CuentaBancaria("Abdiel", 2)
print(cuentaDeBBVA.depositar(500))
print(cuentaDeBBVA.retirar(1000))
print(cuentaDeBBVA.retirar(200))