"""
Enumerate - Enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista) 

for item in lista: # lista não enumerada
    print(item)
for item in lista_enumerada: # lista enumerada
    print(item)

print(lista_enumerada) #retornará o endereço de memória da lista enumerada

#após a conversão da lista teremos, de fato, a lista informada
print(list(enumerate(lista))) #retornará a ordem e os valores da lista

for indice, nome in enumerate(lista): #utilizando o empacotamento para pegar a ordem e o valor
    print(indice, nome)