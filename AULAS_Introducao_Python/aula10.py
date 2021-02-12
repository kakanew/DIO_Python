from datetime import date, time, datetime, timedelta


def trabalhando_com_date():
    data_atual = date.today()
    # print(data_atual.strftime('%d/%m/%Y')
    # print(data_atual.strftime('%d-%m-%Y')
    # print(data_atual.strftime('%A %B %Y'))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    # print(horario.strftime('%H:%M:%S'))
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.date())
    print(data_atual.weekday())
    print(data_atual.month)
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

# ERROS, verificar atualizações

    # data_string = '2019/01/01 12:20:22'
    # data_convertida = datetime.strftime(data_string, '%Y/%m/%d %H:%M:%S')
    # print(data_convertida)
    # print(type(data_convertida))

    # data_criada = datetime - timedelta(days=365, hours=2, minutes=15)
    # print(nova_data)

if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()
