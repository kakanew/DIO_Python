class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminue_canal(self):
        if self.ligada:
            self.canal -= 1
print(__name__)
if __name__ == '__main__':
    televisao = Televisao()
    print('TV está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('TV está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('TV está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('TV está ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminue_canal()
    print('Canal: {}'.format(televisao.canal))
