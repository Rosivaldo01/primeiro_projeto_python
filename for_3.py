#dicionario
produto = {'nome ': 'Caneta Chic','preço': 14.99,
           'importado': True, 'estoque': 793 } 
for chave in produto:
    print(chave)

#Apresenta o nome do produto o impotado (verdade)e valor em estoque
for valor in produto. values():
    print(valor)

for chave, valor in produto. items():
    print(chave, '=', valor)