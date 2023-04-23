# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

# Seria como um não variável, ou seja, seria nada.
# Portanto, ao não digitar nada, irá apresentar a saída abaixo
if not senha:
    print("Você não digitou nada.")


print(not True)  # False
print(not False)  # True