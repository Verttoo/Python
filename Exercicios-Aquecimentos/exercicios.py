x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo Número:"))

print("O Resultado da sua soma e:", x + y)
print("O Resultado da sua subtração e:", x - y)
print("O Resultado da sua multiplicação e:", x * y)
print("O Resultado da sua divisão e:", x / y)
print("O Resultado da sua exponenciação e:", x ** y)

import numpy as np

x = [1,2,3,4,5]

x.append(int(input("Digite o número a ser adicionado:")))

minimo = min(x)
x.remove(minimo)

media = np.mean(x)

print(f'A sua Lista é: {x} E a media da Lista é: {media} E o tamanho da lista é: {len(x)}')

nota = float(input("Digite a nota do aluno:"))

if nota > 7:
    print("Aluno Aprovado")

elif nota < 5:
    print("Aluno Reprovado")

else:
    print("Aluno em Recuperação")

