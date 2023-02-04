"""
CONSTANTE = Variáveis que não vão mudar / colocamos em letra maiúscula
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # 62Km
local_carro = 98 # Km 90 da estrada

RADAR01 = 60 # Velocidade máxima em Km
LOCAL01 = 100 # local do radar Km 100 da estrada
RADAR_RANGE = 1 # A distância que o radar pega

velocidade_check = velocidade > RADAR01
radar01_range = local_carro >= (LOCAL01 - RADAR_RANGE) and local_carro <= (LOCAL01 + RADAR_RANGE)
multa_radar01 = radar01_range and velocidade_check

if velocidade_check:
    print("Velocidade do carro passou do radar 1")

if multa_radar01:
    print("O carro foi multado.")
else:
    print("Carro fora do radar.")
