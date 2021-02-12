# a = 10
# b = 5
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
# print(type(soma))
# soma = str(soma)
# print('soma: ' + str(soma))
# print('subtracao: ' + str(subtracao))
# print(multiplicacao)
# print(divisao)
# print(type(divisao))
# print(int(divisao))
# print(resto)

resultado = ('Soma: {soma} \nSubtração: {sub}'
      '\nMultiplicação: {mult}'
      '\nDivisão: {div}'
      '\nResto: {resto}' .format(soma=soma, sub=subtracao,
                                 div=divisao,
                                 mult=multiplicacao,
                                 resto=resto))
print(resultado)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)