n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if n1 < n2:
    print("O seu segundo número é maior que o primeiro")

elif n1 > n2:
    print("O seu primeiro número é maior que o segundo")
else:
    print("Os números são iguais")

except ValueError:
    print("Digite números.")

