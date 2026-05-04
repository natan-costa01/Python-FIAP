# lista_frutas = ["Banana", "Maçã", "Melancia"]
#
# print(lista_frutas)
#
# lista_frutas.append("Laranja")
# print(lista_frutas)
# print()
#
# for i in range(len(lista_frutas)):
#     print(lista_frutas[i])

nome = ["Ana", "Maria", "Braga", "Enzo", "Leo", "Jailson"]

for i in range(len(nome) - 1):
    for j in range(i + 1, len(nome)):
        print(f"{nome[i]} {nome[j]}")

