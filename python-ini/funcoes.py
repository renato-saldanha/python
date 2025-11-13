def cria_carro(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

cria_carro("Palio", 2000, "AOS-2993", marca="Fiat", motor="1.0", combustivel="Gasolina")
# cria_carro(modelo="Palio", 2000, "AOS-2993", marca="Fiat", motor="1.0", combustivel="Gasolina")

#Todos nomeados
def cria_carros(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

cria_carros(modelo="Palio", ano=2000, placa="AOS-2993", marca="Fiat", motor="1.0", combustivel="Gasolina")