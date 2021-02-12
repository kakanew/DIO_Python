class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b

    def mult(self, valor_a, valor_b):
        return valor_a * valor_b

    def div(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print('Soma: {}' .format(calculadora.soma(10, 2)))
print('Subtração: {}' .format(calculadora.sub(100, 2)))
print('Divisão: {}' .format(calculadora.div(8, 2)))
print('Multiplicação: {}' .format(calculadora.mult(7, 2)))

