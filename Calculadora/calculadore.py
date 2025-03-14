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
        num1 =float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        result = float()
        if operacao == 1:
            result = num1+num2
            print("Resultado: ", result)
        elif operacao == 2:
            result = num1-num2
            print("Resultado: ", result)
        elif operacao == 3:
            result = num1 * num2
            print("Resultado: ", result)
        elif operacao == 4:
            if num2 != 0:
                result = num1 / num2
                print("Resultado: ", result)
            else:
                print("Nao da para dividir por 0")
        else:
            print("Operacao Invalida!")
main()