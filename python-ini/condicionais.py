saldo = 2000
saque = 2000


if saldo == saque:
    print("Sacado Saldo zerado")
elif saldo > saque:
    print("Sacado")
else:
    print("Saldo insuficiente")
    
    
    
#Ternario

status = "Sucesso" if saldo == saque else "Falha"
print(f"Status: {status}")