#sistema de dados de um colaborador

print("=== RELATÓRIO MENSAL DO COLABORADOR ===")

nome = input("Digite o nome do colaborador: ")
valor = float(input("Digite o valor da hora trabalhada em reais (R$) do colaborador: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))
bonus = float(input("Digite o valor fixo do bônus mensal em reais (R$) do colaborador: "))
desconto = float(input("Digite o desconto em reais (R$) do funcionário: "))

sal_bruto = (valor * horas) + bonus
sal_liquido = sal_bruto - desconto

print(f"\n\n========== RELATÓRIO =========="
      f"\nColaborador: {nome.upper()}"
      f"\nO salário bruto do colaborador é: R$ {sal_bruto: .2f}"
      f"\nO salário liquido do colaborador será: R$ {sal_liquido: .2f}")
