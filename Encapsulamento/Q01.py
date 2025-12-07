'''1. Crie uma classe ContaBancaria com um atributo privado __saldo. 
Inicialize o saldo com 0. 
●  Crie métodos depositar(valor) e sacar(valor). 
●  Crie também um método ver_saldo() que retorne o valor do saldo.'''
class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def ver_saldo(self):
        return self.__saldo
    
# Exemplo de uso:
conta = ContaBancaria()
conta.depositar(1000)
conta.sacar(500)
print(f'Saldo atual: {conta.ver_saldo()}')