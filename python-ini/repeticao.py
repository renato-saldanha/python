texto = "Ola mundo, vamos nessa!"
vogais = "AEIOU"

for letra in texto:
    vogal = ''
    if letra.upper() not in vogais:
        vogal += letra 
    
    print(vogal, end="")
else:
    print("Fim")
    
    
print(range(4))
print(list(range(4)))


for numero in range(0, 51, 2):
    print(f"Numero: {numero}")
    
numero = 5    
while numero < 11:
    print(f"numero: {numero}")
    if numero % 5:
        break
    if numero == 5:
        continue  
    numero += 1