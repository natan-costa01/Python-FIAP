print("======= CALCULADORA DE AUMENTO =======")
print()
salario = float(input("Digite o seu salario: "))
print("\n", "======= RESULTADO GERAL =======")

if salario < 280:
    percentual = 0.20
    texto = "20%"
elif salario <= 700:
    percentual = 0.15
    texto = "15%"
elif salario <= 1500:
    percentual = 0.10
    texto = "10%"
else:
    percentual = 0.05
    texto = "5%"

aumento = salario * percentual
salario_final = salario + aumento

print(f"Seu salário era de R$ {salario:.2f}")
print(f"Seu aumento foi de {texto}")
print(f"O valor do aumento foi R$ {aumento:.2f}")
print(f"Seu salário atual é R$ {salario_final:.2f}")
