def calcular(sinal):
    def somar(a,b):
        return float(a+b)
    def subtrair(a,b):
        return a-b
    def multiplicar(a,b):
        return a*b
    def dividir(a,b):
        return a/b
    
    match sinal:
        case "+": return somar
        case "-": return subtrair
        case "*": return multiplicar
        case "/": return dividir
    
print(calcular("*")(2,5))

def pagar_conta(valor):
    return f"Você pagou R${valor:.2f}"

def ver_saldo(saldo):
    return f"Seu saldo é de R${saldo:.2f}"

def iniciar_interacao(funcao_interacao):
    return funcao_interacao(100)


print(iniciar_interacao(pagar_conta))
print(iniciar_interacao(ver_saldo))

def meu_decorator(funcao):
    def envelope():
        print("Faz algo antes")
        funcao()
        print("Faz algo depois")
    return envelope

def ola_mundo():
    print("Olá mundo!")
    
ola_mundo = meu_decorator(ola_mundo)
ola_mundo()
