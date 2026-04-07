print("Digite as notas do aluno")

notas = []

for i in range(4):
    nota = float(input("Nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

#print(f"A média do aluno é: {media})

if media >= 7:
      print(f"Com a média {media} o aluno está aprovado!")
elif media < 7 and media >= 5:
    print(f"Com a média {media} o aluno está em recuperação!")
else:
    print(f"Com a média {media} o aluno está reprovado!")

