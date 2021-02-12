# conjunto = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
# conjunto_uniao = conjunto.union(conjunto2)
# print('União: {}' .format(conjunto_uniao))
# conjunto_interseccao = conjunto.intersection(conjunto2)
# print('Intersecção: {}' .format(conjunto_interseccao))
# conjunto_diferenca1 = conjunto.difference(conjunto2)
# print('Diferença 1 e 2 : {}' .format(conjunto_diferenca1))
# conjunto_diferenca2 = conjunto2.difference(conjunto)
# print('Diferença 2 e 1 : {}' .format(conjunto_diferenca2))
# conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
# print('Diferença simétrica : {}' .format(conjunto_diff_simetrica))

# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4, 5}
# conjunto_subset1 = conjunto_a.issubset(conjunto_b)
# print('Suconjunto a e b : {}' .format(conjunto_subset1))
# conjunto_subset2 = conjunto_b.issubset(conjunto_a)
# print('Suconjunto b e a : {}' .format(conjunto_subset2))
# conjunto_superset1 = conjunto_a.issuperset(conjunto_b)
# print('Superconjunto a e b : {}' .format(conjunto_superset1))
# conjunto_superset2 = conjunto_b.issuperset(conjunto_a)
# print('Superconjunto b e a : {}' .format(conjunto_superset2))

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)