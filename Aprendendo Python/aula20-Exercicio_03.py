primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")
int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)


#if int_primeiro_valor > int_segundo_valor:
#    maior = f"{int_primeiro_valor=}"
#    menor = f"{int_segundo_valor=}"
#else:
#    maior = f"{int_segundo_valor=}"
#    menor = f"{int_primeiro_valor=}"


if primeiro_valor > segundo_valor:
    maior = f"{primeiro_valor=}"
    menor = f"{segundo_valor=}"

else:
    maior = f"{segundo_valor=}"
    menor = f"{primeiro_valor=}"


print(f"{maior} é maior ou igual ao {menor}")