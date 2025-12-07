class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("O saldo não pode ser negativo.")

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