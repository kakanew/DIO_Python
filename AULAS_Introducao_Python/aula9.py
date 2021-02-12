# arquivo = open('teste.txt', 'w')
# arquivo.write('Minha primeira escrita')
# arquivo.close()
#
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nSegunda Linha')
# arquivo.write('\nTerceira Linha\n')
# arquivo.close()

# def escrever_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/teste/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        # print(sum(lista_notas))

def copia_arquivo(nome_arquivo):
    # shutil.copy(nome_arquivo, 'C:/teste')
    shutil.copy(nome_arquivo, 'C:/teste/notas_aluno.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/teste/teste')

if __name__ == '__main__':
    move_arquivo('C:/teste/notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # ler_arquivo('teste.txt')
    # aluno = 'Rafael, 10, 10, 5, 5\n'
    # aluno = 'Felipe, 7, 8, 5, 6\n'
    # aluno = 'Galleane, 7, 9, 8, 6\n'
    # aluno = 'Cesar, 7, 9, 8, 10\n'
    # atualizar_arquivo('notas.txt', aluno)