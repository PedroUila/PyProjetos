"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_b = lista_a faz uma referência direta à variável.
# Portanto se a variável lista_a for alterada no futuro
# a variável lista_b apareceria com a alteração feita

lista_b = lista_a.copy() # É uma copia da lista_a
# e mesmo se a lista_a fo alterada mais a frente do código
# lista_b não será afetada

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
