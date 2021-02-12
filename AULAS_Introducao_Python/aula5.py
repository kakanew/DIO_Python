lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
print(len(lista_animal))

# lista_animal[0] = 'macaco'
# print(lista_animal)

tupla = (1, 10, 12, 14) #imutável
print(tupla[1])
print(len(tupla))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 100
print(lista_numerica)

# print(lista_animal)
# print(lista_animal[1])

# lista.sort()
# lista_animal.sort
# lista_animal
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# for x in lista_animal:
#     print(x)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista))
# print(min(lista))
# print(min(lista_animal))
# print(max(lista_animal))

# if 'gato' in lista_animal:
#     print('Sim existe gato')
# else:
#     print('Não existe gato' )

# if 'lobo' in lista_animal:
#     print('Sim existe lobo')
# else:
#     print('Não existe lobo' )

# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'lobo' in lista_animal:
#     print('Sim existe lobo')
# else:
#     print('Não existe lobo' )
#     lista_animal.append('lobo')
#     print(lista_animal)

# lista_animal.pop()
# print(lista_animal)

# lista_animal.pop(1)
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)
