lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    divisao = 10 / 0
    # numero = lista[3]
    divisao = 10 / 1
    numero = lista[1]
    # x = a
except ZeroDivisionError:
    print('Não é possivel fazer uma divisão por 0')
except ArithmeticError:
    print('Erro ao realizar operaão aritmética')
except IndexError:
    print('Erro ao acessar indice inválido da lista')
except BaseException as ex:
    print('Erro Desconecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
