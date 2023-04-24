"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num = input("Digite um número: ")

# try:
#     int_num = int(num)
#     if int_num % 2 == 0:
#         print("Esse número é PAR.")
#     else:
#         print("Esse número é IMPAR.")
# except:
#     print("Você não digitou um número...")



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input("Informe a hora atual: ")
# try:
#     hora = int(hora)
#     dia = hora >= 5 and hora < 12
#     tarde = hora >= 12 and hora < 18
#     noite = (hora >= 18 or hora < 5) and hora <= 23
#     if dia:
#         print("Bom dia!")
#     elif tarde:
#         print("Boa tarde!")
#     elif noite:
#         print("Boa noite!")
#     else:
#         print("Não conheço essa hora...")
# except:
#     print("Digite apenas as horas.")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome < 5:
        print("Seu nome é curto.")
    elif tamanho_nome > 6:
        print("Seu nome é muito grande.")
    else:
        print("Seu nome é normal.")
else:
    print("Digite seu nome.")
