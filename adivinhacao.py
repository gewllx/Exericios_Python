import random

numero_secreto = random.randint(1, 1000)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número secreto entre 1 e 1000: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")