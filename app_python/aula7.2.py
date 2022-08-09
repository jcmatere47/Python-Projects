class Calculadora:
    def __init__(self):
        pass
# sem o init roda do mesmo jeito

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    # def subtracao(self, valor_a, valor_b):
    #     return self.a - self.b
    #
    # def multiplicacao(self, valor_a, valor_b):
    #     return self.a * self.b
    #
    # def divisao(a, b):
    #     return a / b

calculadora = Calculadora()
print(calculadora.soma(10, 5))
