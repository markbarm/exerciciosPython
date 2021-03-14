#Ler dois vetores de dimensão 5 e calcular o produto interno deles.
vetor1 = []
vetor2 = []
produtoInterno = 0.0
print("insira as componentes do primeiro vetor: ")
for i in range(5):
    vetor1.append(float(input(f'Entre com o {i+1}-ésimo valor do vetor 1: ')))
print("insira as componentes do segundo vetor: ")
for i in range(5):
    vetor2.append(float(input(f'Entre com o {i+1}-ésimo valor do vetor 1: ')))
#cálculo do produto interno
for i in range(5):
    produtoInterno += vetor1[i]*vetor2[i]
print(f'o produto interno é {produtoInterno:.2f}')
