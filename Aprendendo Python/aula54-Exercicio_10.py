"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ["Maria", "Pedro", "Ninguém","Joaquim", "Rochele"]
lista.append("Otávio")
quant_pessoas = range(len(lista))

for indice in quant_pessoas:
    print(f"Pessoa do índice {indice}: {lista[indice]}")