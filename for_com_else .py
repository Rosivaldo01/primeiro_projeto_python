PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = {
    'João gosta de futebol e política',
    'A praia foi divertida'
}
for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui pelo menos uma palavara proibida:', palavra)
            found = True
            break

    else:
        print('O texto esta autorizado:', texto)
