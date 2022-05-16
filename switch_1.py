def get_dia_semana(dia):
    dias = { 
        1: 'Dominogo',
        2: 'Segundo',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7 : 'Sabado'
    }
    return dias.get (dia, '** inválido **')
if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}:{get_dia_semana(dia)}')
