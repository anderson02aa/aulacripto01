import math
class GeometricaColunar:

    def criptografar(self, texto):
        texto = texto.replace(' ', '').upper()
        res = ""
        for j in range(0, 8):
            for i in range(j, len(texto), 8):
                res += texto[i]

        for i in range(0, self.calcularlinha(texto)-len(texto)):
            res += "X"
        return res

    def decriptografar(self, texto):
        texto = texto.replace(' ', '').upper()
        res = ""
        for j in range(0, 4):
            for i in range(j, len(texto)-1, 4):
                res += texto[i]
        return res

    def calcularlinha(self, texto):
        texto = texto.replace(' ', '').upper()
        return int((math.ceil(len(texto) / 8)) * 8)

print("PROGRAMA DE CIFRA DE TRANSPOSIÇÃO")
print("ALFABETO DISPONIVEL [ABCDEFGHIJKLMNOPQRSTUVWXYZ]")
print("")
while True:
    print("")
    txt = input("Entre com o texto: ")
    resp = int(input("[1] Criptografar [2] Decriptografar -- Qualquer outro valor encerra o programa"))
    if resp==1:
        print("Resultado: ", GeometricaColunar().criptografar(txt))
    elif resp==2:
        print("Resultado: ", GeometricaColunar().decriptografar(txt))
    else:
        break

    print("")
    print("")