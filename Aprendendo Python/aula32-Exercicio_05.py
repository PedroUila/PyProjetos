# num = input("Digite um número: ")

# try:
#     int_num = int(num)
#     if int_num % 2 == 0:
#         print("Esse número é PAR.")
#     else:
#         print("Esse número é IMPAR.")
# except:
#     print("Você não digitou um número...")



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




