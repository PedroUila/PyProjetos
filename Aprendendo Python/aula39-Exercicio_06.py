"""
Iterando strings
"""

nome = input("Digite seu nome aqui: ")
novo_nome = ""
tamanho_nome = len(nome)
contador = 0

while contador < tamanho_nome:
    novo_nome += nome[contador] + "*"
    contador += 1

print(novo_nome)
