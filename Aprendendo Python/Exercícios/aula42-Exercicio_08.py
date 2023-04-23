frase = "Python é uma linguagem de programação multiparadigma. " \
        "Python foi criado por Guido van Rossum."

abc = "abcdefghijklmnopqrstuvwxyz"
indice = 0
maior_quantidade = 0

while indice < len(abc):
    contagem_letras = frase.count(abc[indice])
    if contagem_letras > maior_quantidade:
        maior_quantidade = contagem_letras
        letra_mais_escrita = abc[indice]
    print(f"{abc[indice]} = {contagem_letras}")
    indice += 1

if maior_quantidade >= 2:
    print (f"\nA letra {letra_mais_escrita} apareceu {maior_quantidade} vezes na frase.")
elif maior_quantidade == 1:
    print (f"{letra_mais_escrita} = {maior_quantidade} vez")
elif maior_quantidade == 0:
    print("Nenhuma frase foi escrita.")

print("\nFim do programa.")

