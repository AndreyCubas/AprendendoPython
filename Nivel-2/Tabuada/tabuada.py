num = float(input("Digite um Numero e veja sua tabuada: "))
def tabuada (num):
    for contador in range (1,11):
        resultado = num * contador
        print(f"{num} X {contador} = {resultado}")
tabuada(num)