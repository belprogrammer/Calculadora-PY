num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))

print("Escolha a operação desejada:")
print("1 - Adição")
print("2- Subtração")
print("3 - Multplicação")
print("4 - Divisão")
print("5- Potenciação")
print("6- Raiz Quadrada")
print("7- Sair")

operacao = input("Digite o número da operação desejada: ")

if operacao == '1':
    resultado = num1 + num2
    print(f"Seu resultado é: {resultado}")

elif operacao == '2':
    resultado = num1 - num2
    print(f"Seu resultado é: {resultadso}")

elif operacao == '3' :
    resultado = num1 * num2
    print(f"Seu resultado é: {resultado}")      

    if  operacao == '4':
     if num2 != 0:           
        resultado = num1 / num2
        print(f"Seu resultado é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")


        if operacao == '5':
            resultado = num1 ** num2    
            print(f"Seu resultado é: {resultado}")
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")

        if operacao == '6':
            if num1 >= 0:
                resultado = num1 ** 0.5
                print(f"Seu resultado é: {resultado}")
            else:
                print("Não é possível calcular a raiz quadrada de um número negativo.")

                if operacao == '7':
                    print("Saindo da calculadora. Até logo!")   
