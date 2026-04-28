n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
operação = input("Digite uma operação matematica (/, *, +, -) : ")

faz = 0

if operação == "/":
    faz = n1 / n2
    print(f"A divisão é: {faz}")
elif operação == "*":
    faz = n1 * n2
    print(f"A multiplicação é: {faz}")
elif operação == "+":
    faz = n1 + n2
    print(f"A soma é: {faz}")
elif operação == "-":
    faz = n1 - n2
    print(f"A subtração é: {faz}")
else:
    print("Digite um valor valido")

