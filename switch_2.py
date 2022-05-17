def get_tipo_dia(dia):
    dias = {
    1: "Fim de semana",
    2: "Dia de semana",
    3: "Dia de seman",
    4: "Dia de seman",
    5: "Dia de seman",
    6: "Dia de seman",
    7: "Fim de semana"
    }
    return dias.get(dia, '**inválido**')

if __name__ =="__main__":
    for dia in range (8):
         print(f'{dia}: {get_tipo_dia(dia)}')
    