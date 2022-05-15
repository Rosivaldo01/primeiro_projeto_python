palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')
print('fim')

aprovados = ['Rafaela', 'Renato', 'Pedro', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate (aprovados):
    print(f'{posicao + 1})', nome)

dia_semana = ('Domino', 'Segunda', 'Terça', 
              'Quarta', 'Quinta', 'Sexta','Sábado')
for dia in dia_semana:
    print(f'Hoje é {dia}')

for numero in {1,2,3,4,5,6}:
    print(numero)

