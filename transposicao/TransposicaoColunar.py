import math
class TransColunar:

    def calcularlinha(self, texto, chave):
        chave = chave.replace(' ', '').upper()
        texto = texto.replace(' ', '').upper()
        return int((math.ceil(len(texto) / len(chave))) * len(chave))

    def criptografar(self, texto, chave):
        texto = texto.replace(' ', '').upper()
        chave = chave.replace(' ', '').upper()
        chave1 = list(chave)
        chave1 = sorted(set(chave1))
        chave1 = ''.join(chave1)
        res = ""
        for i in range(0, self.calcularlinha(texto, chave)-len(texto)):
            texto += "Z"
        for k in range (0, len(chave1)):
            for l in range(0, len(chave)):
                if (chave1[k].find(chave[l]) >= 0):
                    m = l
                    for i in range(m, len(texto), len(chave)):
                        res += texto[i]


        return res


print("PROGRAMA DE CIFRA DE TRANSPOSIÇÃO COLUNAR")
print("ALFABETO DISPONIVEL [ABCDEFGHIJKLMNOPQRSTUVWXYZ]")
print("")
while True:
    print("")
    txt = input("Entre com o texto: ")
    chave = input("Entre com a chave: ")
    resp = int(input("[1] Criptografar -- Qualquer outro valor encerra o programa"))
    if resp==1:
        print("Resultado: ", TransColunar().criptografar(txt, chave))
    else:
        break

    print("")
    print("")
