""" Calculadora com while """

while True:
    print("[+]soma [-]subtracao [x]multiplicação [/]divisão")
    operacao = input("Digite a operação que deseja fazer: ").lower()
    soma = operacao == "+"
    subtracao = operacao == "-"
    multiplicacao = operacao == "x"
    divisao = operacao == "/"
    operacao_valida = soma or subtracao or multiplicacao or divisao

    if not(operacao_valida):
        print("\nNão compreendi a operação.\n")
        continue
        
    while True:
        try:
            num1 = input("Digite um número: ")
            num1 = int(num1)
            num2 = input("Digite outro número: ")
            num2 = int(num2)
            break
        except:
            print("Digite números apenas.")

    resultado = None

    if soma:
        resultado = num1 + num2
    elif subtracao:
        resultado = num1 - num2
    elif multiplicacao:
        resultado = num1 * num2
    elif divisao:
        resultado = num1 / num2
    
    print(f"O resultado é {resultado}")


    while True:
        sair = input("Deseja encerrar o programa? [s]im [n]ão: ")
        print("\n")
        sair = sair.lower()
        if sair == "s" or sair == "n":
            break
        else:
            print("Digite s ou n...")
    
    if sair == "s":
        break


print("Programa encerrado!")