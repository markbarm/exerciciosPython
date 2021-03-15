lista = [0 for _ in range(10)]
for i in range(10):
    lista[i] = int(input())
maior = 0
posicao = 0
for j in range(10):
    if lista[j] >= maior:
        maior = lista[j]
        posicao = j
print(maior, j)



