pessoa = {"nome": "Renato", 
          "idade": 34,          
        }

print(pessoa["nome"])

carro = dict(modelo="Corsa", marca="Chevrolet")

print(carro["marca"])

carro["cilindrada"] = 145

print(carro)


pessoas = {
            "gerente": {"nome": "Renato", "idade": 34},
            "comercial": {"nome": "Maria", "idade": 22}, 
        }

print(f"Idade comercial: {pessoas["comercial"]["idade"]}")


for pessoa in pessoas:
    print(f"For: {pessoa, pessoas[pessoa]}")
    
    

for chave, valor in pessoas.items():
    print(f"Chave Valor: {chave, valor}")
    
    
print(pessoas.get("nome"))