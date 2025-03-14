import random

def jogar():
    num = random.randint(1, 100)
    tentativas = 0
    print("Seja bem vindo ao jogo de advinhacao")
    print("Tente advinhas um numero de 0 a 100")
    while True: 
        chance = int(input("Digite seu palpite: "))
        tentativas += 1
        if chance < num :
            print("O numero e MAIOR!")
        elif chance > num:
            print("O numero e MENOR!")
        else:
            print("Parabens voce acertou o numero")
            break
jogar()