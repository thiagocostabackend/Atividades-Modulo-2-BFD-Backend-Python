from abc import ABC, abstractmethod
from typing import List
from datetime import date


# ---------- Interfaces / Abstrações ----------
class Cancelavel(ABC):
    @abstractmethod
    def cancelar_pagamento(self) -> bool:
        """Tenta cancelar o pagamento. Retorna True se cancelado com sucesso."""
        pass


class Pagamento(ABC):
    def __init__(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero.")
        self.valor = float(valor)
        self.processado = False
        self.cancelado = False
        self.data_processamento = None

    @abstractmethod
    def processar_pagamento(self) -> bool:
        """Processa o pagamento. Retorna True se processado com sucesso."""
        pass

    # opcional: representação amigável
    def __repr__(self):
        status = "processado" if self.processado else ("cancelado" if self.cancelado else "pendente")
        return f"<{self.__class__.__name__} valor={self.valor:.2f} status={status}>"


# ---------- Implementações concretas ----------
class CartaoCredito(Pagamento, Cancelavel):
    def __init__(self, valor: float, titular: str, numero_cartao: str, cvv: str, validade: str):
        super().__init__(valor)
        self.titular = titular
        self.numero_cartao = numero_cartao
        self.cvv = cvv
        self.validade = validade  # string MM/AA por exemplo

    def processar_pagamento(self) -> bool:
        if self.cancelado:
            print("Pagamento com cartão já cancelado; não pode processar.")
            return False
        if self.processado:
            print("Pagamento com cartão já foi processado.")
            return False
        # aqui normalmente você chamaria um gateway; vamos simular validação simples
        if len(self.numero_cartao) < 12:
            print("Número de cartão inválido.")
            return False
        self.processado = True
        self.data_processamento = date.today()
        print(f"[Cartão] Pagamento de R${self.valor:.2f} processado para {self.titular}.")
        return True

    def cancelar_pagamento(self) -> bool:
        if not self.processado:
            print("Não há pagamento com cartão processado para cancelar.")
            return False
        if self.cancelado:
            print("Pagamento com cartão já cancelado.")
            return False
        # aqui normalmente reverteria via gateway
        self.cancelado = True
        print(f"[Cartão] Pagamento de R${self.valor:.2f} cancelado.")
        return True


class Pix(Pagamento, Cancelavel):
    def __init__(self, valor: float, chave_pix: str):
        super().__init__(valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self) -> bool:
        if self.cancelado:
            print("Pagamento via Pix já cancelado; não pode processar.")
            return False
        if self.processado:
            print("Pagamento via Pix já foi processado.")
            return False
        # simulação: chave pix deve ter pelo menos 5 caracteres
        if len(self.chave_pix.strip()) < 5:
            print("Chave PIX inválida.")
            return False
        self.processado = True
        self.data_processamento = date.today()
        print(f"[Pix] Pagamento de R${self.valor:.2f} enviado para chave {self.chave_pix}.")
        return True

    def cancelar_pagamento(self) -> bool:
        # em muitos casos Pix não é cancelável após liquidação, mas vamos permitir a simulação
        if not self.processado:
            print("Não há pagamento via Pix processado para cancelar.")
            return False
        if self.cancelado:
            print("Pagamento via Pix já cancelado.")
            return False
        self.cancelado = True
        print(f"[Pix] Pagamento de R${self.valor:.2f} cancelado (simulação).")
        return True


class Boleto(Pagamento, Cancelavel):
    def __init__(self, valor: float, cpf_cnpj: str):
        super().__init__(valor)
        self.cpf_cnpj = cpf_cnpj
        self.numero_boleto = None

    def emitir_boleto(self) -> str:
        # gera um número de boleto simplificado (apenas para simulação)
        if not self.numero_boleto:
            self.numero_boleto = f"2379{int(self.valor*100):06d}{self.cpf_cnpj[-4:]}"
        return self.numero_boleto

    def processar_pagamento(self) -> bool:
        # No mundo real o boleto é pago pelo cliente e depois compensado.
        if self.cancelado:
            print("Boleto cancelado; não pode processar.")
            return False
        if self.processado:
            print("Boleto já compensado/processado.")
            return False
        # simulação: emitir boleto e marcar como "processado" (compensado)
        self.emitir_boleto()
        self.processado = True
        self.data_processamento = date.today()
        print(f"[Boleto] Boleto {self.numero_boleto} no valor de R${self.valor:.2f} compensado.")
        return True

    def cancelar_pendente(self) -> bool:
        """Cancelar antes de ser compensado (por exemplo, cliente não pagou)."""
        if self.processado:
            print("Boleto já compensado, não é possível cancelar via cancelar_pendente().")
            return False
        self.cancelado = True
        print(f"[Boleto] Boleto {self.emitir_boleto()} cancelado (pendente).")
        return True

    def cancelar_pagamento(self) -> bool:
        # se já compensado, aqui simulamos que não é possível cancelar via sistema simples
        if not self.processado:
            print("Boleto ainda não compensado; use cancelar_pendente() se quiser cancelar emissão.")
            return False
        if self.cancelado:
            print("Boleto já cancelado.")
            return False
        # simulação: cancelar compensação
        self.cancelado = True
        print(f"[Boleto] Cancelamento de compensação do boleto {self.numero_boleto} efetuado (simulação).")
        return True


# ---------- Pequeno gestor de pagamentos ----------
class PaymentGateway:
    def __init__(self):
        self.pagamentos: List[Pagamento] = []

    def adicionar_pagamento(self, p: Pagamento):
        self.pagamentos.append(p)
        print(f"Adicionado: {p}")

    def processar_todos(self):
        for p in self.pagamentos:
            p.processar_pagamento()

    def listar_pagamentos(self):
        for p in self.pagamentos:
            print(p)

    def cancelar_todos_processados(self):
        for p in self.pagamentos:
            if p.processado and not p.cancelado:
                if isinstance(p, Cancelavel):
                    p.cancelar_pagamento()


# ---------- Exemplo de uso ----------
if __name__ == "__main__":
    gateway = PaymentGateway()

    c = CartaoCredito(150.0, "Thiago Mouzinho", "123456789012", "123", "12/27")
    px = Pix(50.5, "thiago@pix")
    b = Boleto(200.0, "12345678901")

    gateway.adicionar_pagamento(c)
    gateway.adicionar_pagamento(px)
    gateway.adicionar_pagamento(b)

    print("\nProcessando todos os pagamentos...")
    gateway.processar_todos()

    print("\nLista após processamento:")
    gateway.listar_pagamentos()

    print("\nTentando cancelar pagamentos processados:")
    gateway.cancelar_todos_processados()

    print("\nLista final:")
    gateway.listar_pagamentos()
