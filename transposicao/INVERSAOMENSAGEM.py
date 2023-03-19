print("PROGRAMA DE INVERSÃO DE MENSAGEM")
while True:
    text = ""
    frase = input('Digite uma frase: ')
    print(' Você digitou: {}'.format(frase))
    for palavra in frase.split(" "):
        text += palavra[::-1]+" "
    print('Frase invertida: {}'.format(text))
    print("")
    resp = int(input("Continuar [0] - Qualquer outro caractere encerrará"))
    if resp !=0:
        break