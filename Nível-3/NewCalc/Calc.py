def somar(num1, num2):
    result = num1 + num2
    print(f"Resultado: {result}")
    return result

def subtrair (num1, num2):
    result = num1-num2
    print(f"Resultado: {result}")
    return result

def multiplicar (num1,num2):
    result = num1 * num2
    print(f"Resultado: {result}")
    return result

def dividir (num1, num2):
    result = num1/num2
    print(f"Resultado: {result}")
    return result

def main():
        
        while True:
            print("Escolha a operação desejada:")
            print("1. Adição")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("5. Sair")
            operacao =int(input("Digite a opcao desejada: "))
            if operacao == 5:
                print("Saindo da Calculadora")
                break
            elif operacao >= 6 or operacao <= 0:
                print("Opercao Invalida!")
                continue
            num1 =float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            if operacao == 1:
                somar(num1, num2)
            elif operacao == 2:
                subtrair(num1, num2)
            elif operacao == 3:
                multiplicar(num1, num2)
            elif operacao == 4:
                if num2 != 0:
                    dividir(num1, num2)
                else:
                    print("Nao da para dividir por 0")
main()  