"""
Introdução ao empacotamento e desempacotamento
"""

""" O empacotamento você atribui um valor da lista a uma variável.
No caso abaixo, os underlines indicam que o valores daquela posição
não irão receber nenhuma variável, equanto a variável nome terá o 
valor Helena e o resto é a lista"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)