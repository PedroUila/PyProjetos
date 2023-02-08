""" Calculadora com while """

from time import sleep

while True:
    while True:
        print("[+]soma [-]subtracao [x]multiplicação [/]divisão")
        operacao = input("Digite a operação que deseja fazer: ").lower()
        soma = operacao == "+"
        subtracao = operacao == "-"
        multiplicacao = operacao == "x"
        divisao = operacao == "/"

        if soma or subtracao or multiplicacao or divisao:
            break
        else:
            print("\nNão compreendi.\n")

    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    num1 = int(num1)
    num2 = int(num2)

    if soma:
        print(num1 + num2)
    elif subtracao:
        print(num1 - num2)
    elif multiplicacao:
        print(num1 * num2)
    elif divisao:
        print(num1 / num2)
    
    sair = input("Deseja encerrar o programa? [s]im [n]ão: ")
    print("\n")
    sair = sair.lower()
    if sair == "s":
        break
    elif sair != "s" and sair != "n":
        print("Digite s ou n...")
        continue
print("Programa encerrado!")