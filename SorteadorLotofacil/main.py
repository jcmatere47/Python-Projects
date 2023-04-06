
import random

numeros_sorteados = []

while len(numeros_sorteados) < 15:
    numero = random.randint(1, 25)
    if numero not in numeros_sorteados:
        numeros_sorteados.append(numero)

numeros_sorteados.sort()

print("Números sorteados em ordem crescente:")
print(numeros_sorteados)