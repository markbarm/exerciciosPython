notas = []
numero = int(input("Entre com o número de notas: "))
for i in range(numero):
    nota = float(input(f'Nota {i+1}: '))
    notas.append(nota)
print(notas)
