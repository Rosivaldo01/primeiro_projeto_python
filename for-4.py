for i in range (1 , 10):
    #neste caso não será informado o else.
    if i == 6: 
        break
    print(i)
else:
    print ('fim!')



from random import randint
def sortear_dado ():
    return randint(1, 6)

for i in range (1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado()== i:
        print('Acertou ', i)
        break
    else:
        print('Não acertou o número')
        
            




