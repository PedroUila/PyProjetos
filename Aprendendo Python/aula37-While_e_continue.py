"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6: # irá passar o 6 e imprimir os outros números
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27: # irá passar do 10 ao 27 e vai imprimir os outros números
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')