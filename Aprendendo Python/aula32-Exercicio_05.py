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
#     noite = hora >= 18 or hora < 5
#     if dia:
#         print("Bom dia!")
#     elif tarde:
#         print("Boa tarde!")
#     elif noite:
#         print("Boa noite!")
# except:
#     print("Digite apenas as horas.")



nome = input("Digite seu primeiro nome: ")
try:
    if len(nome) < 5:
        print("Seu nome é curto.")
    elif len(nome) > 6:
        print("Seu nome é muito grande.")
    else:
        print("Seu nome é normal.")
except:
    print("Digite seu nome.")



