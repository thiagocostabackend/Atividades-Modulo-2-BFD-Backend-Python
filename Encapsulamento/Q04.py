'''4.Crie uma classe Produto com atributos privados __nome e __preco. 
O nome só pode ser lido, não alterado. 
●  O preço pode ser lido e alterado, mas não pode ser negativo. 
●  Use @property e @setter.'''
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.") # raise ValueError faz com que o programa lance um erro caso o preço seja negativo.
        self.__preco = novo_preco

# Exemplo de uso:
produto = Produto("Caneta", 2.50)
print(produto.nome)  # Saída: Caneta
print(produto.preco)  # Saída: 2.5

produto.preco = 3.00
print(produto.preco)  # Saída: 3.0

produto.preco = -1.00  # Isso levantará um ValueError