"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration: # nome do erro (no caso, o StopIteration) que o try irá tratar
#         break


# Tudo o que acima é o for abaixo (for é bem mais simples! muito bom!)
for letra in texto:
    print(letra)