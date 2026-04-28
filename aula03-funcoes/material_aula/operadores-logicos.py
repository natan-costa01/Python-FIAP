#LÓGICA E (AND)
from scipy.stats import false_discovery_control

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print("\n",verifica_login)

if verifica_login:
    print("Entrar no programa!")

#LÓGICA OU (OR)

logica_ou = False or True
print("\n", logica_ou)

#OPERADOR DE NEGAÇÃO (NOT)

negacao = not False
print(negacao)

if not verifica_login:
    print("loga certo ai....")
