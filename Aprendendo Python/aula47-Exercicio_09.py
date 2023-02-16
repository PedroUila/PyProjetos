"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""



while True:
    palavra_secreta = input("Digite a palavra que será advinhada: ").lower()
    if " " in palavra_secreta:
        print("Digite uma palavra sem espaços.")
        print("\n")
        continue
    elif palavra_secreta == "":
        print("Você não digitou nenhuma palavra.")
        print("\n")
        continue
    elif not palavra_secreta.isalpha():
        print("Digite uma palavra sem números, por favor.")
        print("\n")
        continue
    elif len(palavra_secreta) == 1:
        print("Digite uma palavra, por favor")
        print("\n")
        continue
    
    tentativas = ""
    quant_tentativas = 0
    while True:
        
        letra = input("Digite uma letra para descobrir a palavra secreta: ").lower()
        if " " in letra:
            print("Digite apenas uma letra sem espaços, por favor.")
            print("\n")
            continue
        elif letra == "":
            print("Você não digitou nenhuma letra.")
            print("\n")
            continue
        elif not letra.isalpha():
            print("Digite uma letra e sem números.")
            print("\n")
            continue
        elif len(letra) > 1:
            print("Digite apenas uma letra.")
            print("\n")
            continue
        elif letra in tentativas:
            print("Você já digitou essa letra. Tente outra letra.")
            continue

        tentativas += letra
        palavra_tentativa = ""
        for letra_secreta in palavra_secreta:
            if letra_secreta in tentativas:
                palavra_tentativa += letra_secreta
            else:
                palavra_tentativa += "*"
        if letra in palavra_secreta:
            print(f"Boa! A palavra possui {letra}")
        else:
            print(f"Ops, a palavra NÃO possui {letra}")
        print(f"\n## Palavra secreta ##\n{palavra_tentativa}")
        quant_tentativas += 1
        if palavra_tentativa == palavra_secreta:
            print("Parabéns! Você adivinhou qual era a palavra!")
            print(f"Você acertou depois de {quant_tentativas} tentativas")
            break
        
    # bloco para checar a saída
    while True:
        jogar_novamente = input("Deseja jogar novamente? [s]im [n]ão ").lower()
        if jogar_novamente != "s" and jogar_novamente != "n":
            print("Digite s para jogar novamente, ou n caso deseje sair.")
            print("\n")
            continue
        break
    if jogar_novamente == "n":
        break
    print("\n")
    continue

print("\n")
print("=" * 30)
print("Fim do programa!! :)")
print("=" * 30)