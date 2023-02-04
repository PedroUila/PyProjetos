"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = "a"
v2 = "b"

print (id(v1))
print (id(v2))

print(30 * "#")

condicao = False
passou_no_if = None # isso seria uma flag, um valor que será usado depois

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
