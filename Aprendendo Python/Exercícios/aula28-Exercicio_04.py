"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

if not nome or not idade:
    print("Desculpe... você deixou campos em vazio.")
else:
    nome_invertido = nome[::-1]

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")

    if " " in nome:
        print("O nome digitado possui espaços.")
    else:
        print("O nome digitado NÃO possui espaços.")

    print(f"Seu nome tem {len(nome)} dígitos (com ou sem espaços).")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")





