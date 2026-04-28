print("Ola, Mundo")
msg = "Ola, Mundo"
i = int(input("Digite 1 para continuar e 2 para parar:"))

while i == 1:
    print(msg)
    i = int(input("Digite 1 para continuar e 2 para parar:"))

    if i  == 2:
        print("\nFim")
        break