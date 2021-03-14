#Ler dois vetores com 5 inteiros cada e compare se tem elementos em comum.
vetor1 = []
vetor2 = []
for i in range(5):
    vetor1.append(int(input(f'Entre com o {i+1}-ésimo valor do vetor 1: ')))
print()
for i in range(5):
    vetor2.append(int(input(f'Entre com o {i+1}-ésimo valor do vetor 2: ')))

umEmComum = False
for x in vetor1:
    for y in vetor2:
        if x == y:
            umEmComum = True
            print(f'O elemento {x} é um elemento em comum dos dois vetores')
print()
if not umEmComum:
    print('Nenhum elemento em comum')
