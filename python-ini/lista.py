frutas = ["laranja", "maçã", "goiaba"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 420000, 2020, 2900, "Cuiabá", True]
matriz = [     ["a","b","c"], [1, "v", 2], ["9", "u", 10]     ]

print(f"Matriz: {matriz[1:]}")
lista = ["P", "y", "t", "h", "o", "n"]
print(f"Lista: {lista[:1]}")
print(f"Lista: {lista[0:3:2]}")
print(f"Lista: {lista[::]}")
print(f"Lista: {lista[::-1]}")
print(f"Lista: {lista[1:4:1]}")

lista = []
lista.append(1)
lista.append("Renato")

print(f"Lista A: {lista}")

#lista.clear()
#lista.copy()

lista_b = lista
lista_c = lista.copy()
lista_b.clear()
print(f"Lista B: {lista_b}")
print(f"Lista C: {lista_c}")

cores = ["azul", "vermelho", "amarelo", "azul"]

print(f"Qtde Azul: {cores.count("azul")}")

print(f"Qtde Vermelho: {cores.count("vermelho")}")

cores.extend(["rosa", "marrom"])

print(f"Cores a mais: {cores}")

print(f"Index Marrom: {cores.index("marrom")}")

#lista.pop -> retira o ultimo indice
#lista.pop(index)
#lista.remove("objeto") retira o objeto em sí
#lista.revese()
#lista.sort() -> ordem alfabetica
#lista.sort(reverse=True) -> reverte a lista
#lista.sort(key=lambda x: len(x)) -> ordena por tamanho de cada objeto
#lista.sort(key=lambda x: len(x), reverse=True) -> ordena por tamanho de cada objeto e reverte a lista

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])