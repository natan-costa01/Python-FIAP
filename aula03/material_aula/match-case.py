escolha_usuario = 0
# 0 sair do prgrama
# 1 entrar no programa
# >>>> erro!

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!")