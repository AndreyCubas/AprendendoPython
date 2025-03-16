temperatura = float(input("Digite a Temperatura Registrada: "))
print("Sua temperatura seria Celcius ou Farenheit?")
print("1-Celcius")
print("2-Farenheit")
opcao = int(input("Escolha a Opcao: "))
3056
def conversorTf (temperatura):
    Tc = (temperatura*1.8)+32
    return Tc
def conversorTc (temperatura):
    Tf = ((temperatura-32)*5)/9
    return Tf

if opcao == 1:
    print(f"A Temperatura em Farenheit: {conversorTf(temperatura)}")
elif opcao == 2:
    print(f"A Temperatura em Celcius: {conversorTc(temperatura)}")
else:
    print("Opcao Invalida")