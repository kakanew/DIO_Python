class Error(Exception):
    pass
class InputError(Error):
     def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Nota de 0 à 10: '))
        print(x)
        if x > 10:
           raise InputError('Nota não pode ser maior qur 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor qur 10')
        break
    except ValueError:
        print('Valor Invalido. Digitar apenas números.')
    except InputError as ex:
        print(ex)