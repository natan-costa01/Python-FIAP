votacao_idade = int(input("Digite a sua idade: "))

if votacao_idade >= 16 and votacao_idade < 18:
    print("Seu voto é opcional, mas pode retirar o titulo.")
elif votacao_idade >= 18 and votacao_idade <= 70:
    print("Seu voto é obrigatorio.")
elif votacao_idade > 70:
    print("Não precisa mais votar")
else:
    print("Voto proibido.")