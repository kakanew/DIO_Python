class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def mult(self):
        return self.valor_a * self.valor_b

    def div(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print('Valor 1: {}' .format(calculadora.valor_a))
    print('Valor 2: {}' .format(calculadora.valor_b))
    print('Soma: {}' .format(calculadora.soma()))
    print('Subtração: {}' .format(calculadora.sub()))
    print('Divisão: {}' .format(calculadora.div()))
    print('Multiplicação: {}' .format(calculadora.mult()))

# def soma(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mult(a, b):
#     return a * b
#
# def div(a, b):
#     return a / b
#
# print(div(8, 4))
# print(soma(8, 4))
# print(sub(8, 4))
# print(mult(8, 4))