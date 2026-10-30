#Jogo de adivinhação: o programa sorteia um número de 1 a 100 e dá dicas "maior" ou "menor" até você acertar

import random

segredo = random.randint(1, 100)
chute = 0
tentativas = 0

while chute != segredo:
    chute = int(input("Tente acertar o número: "))
    tentativas += 1

    if chute < segredo:
        print("O número secreto é maior. Tente novamente.")
    elif chute > segredo:
        print("O número secreto é menor. Tente novamente.")
    else:
        print(f"Você acertou em {tentativas} tentativas!")