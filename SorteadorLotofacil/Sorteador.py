import random

numeros_sorteados = []

# loop para sortear 15 números aleatórios
for i in range(15):
    numero = random.randint(1, 25)
    numeros_sorteados.append(numero)

# ordena os números em ordem crescente
numeros_sorteados.sort()

# imprime a lista de números sorteados em ordem crescente
print("Números sorteados em ordem crescente:")
print(numeros_sorteados)
