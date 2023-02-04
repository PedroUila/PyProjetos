num = input("Digite um número: ")

try:
    int_num = int(num)
    if int_num % 2 == 0:
        print("Esse número é PAR.")
    else:
        print("Esse número é IMPAR.")

except:
    print("Você não digitou um número...")


