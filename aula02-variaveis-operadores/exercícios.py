#área de um círculo
from pywin.framework.interact import valueFormatOutputError

raio = input("Digite o valor do raio: ")
pi = 3.14159
area = float(pi) * (float(raio)**2)

print(f"A área da circunferência é {area}")

#temperatura de fahrenheit para celsius
fah = input("Digite a temperatura em Fahrenheit: ")
celsius = (float(fah) - 32) * 5/9

print(f"A temperatura em celsius é de {celsius}°")

#compra de itens

total_gasto = 0

while True:
    nome_item = input("Digite o nome do item (ou 'sair' para finalizar): ")
    if nome_item.lower() == 'sair':
        break

    try:
        quantidade = int(input(f"Digite a quantidade de {nome_item}: "))
        preco_unitario = float(input(f"Digite o preço unitário de {nome_item}: R$ "))

        custo_item = quantidade * preco_unitario
        total_gasto += custo_item
        print(f"Custo de {nome_item}: R$ {custo_item:.2f}\n")

    except ValueError:
        print("Entrada inválida. Por favor, insira números para quantidade e preço.")

print(f"Você gastou {total_gasto:.2f} R$")

#velocidade do carro

vel_inicial = input("Digite a distância percorrida: ")
vel_media = 60

horas = float(vel_inicial) / vel_media

h = int(horas)  # parte inteira (horas)
m = int((horas - h) * 60)  # parte decimal convertida em minutos

print(f"Você andou por {h} hora(s) e {m} minuto(s)!")

#notas de alunos

notas = []

nome_aluno = input("Digite o nome do aluno (ou digite 'sem aluno' para finalizar): ")

if nome_aluno.lower() == 'sem aluno':
    print("Programa encerrado.")
else:
    while True:
        try:
            nota = float(input(f"Digite a nota de {nome_aluno} (ou -1 para parar): "))

            if nota == -1:
                break

            notas.append(nota)

        except ValueError:
            print("Digite um número.")

    media = sum(notas) / len(notas)
    print(f"A média de {nome_aluno} é {media}!")

#media ponderada

nome_aluno02 = input("Digite o nome do aluno (ou digite 'sem aluno' para finalizar): ")

notas02 = []
pesos02 = []

for i in range():
    nota02 = float(input("Digite a nota: "))
    peso02 = float(input("Digite o peso: "))

    notas02.append(nota)
    pesos02.append(peso)

media_ponderada = sum(notas02*pesos02) / sum(pesos02)

print(f"A média ponderada de {nome_aluno02} é {media_ponderada}!")

