from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail:  ")
    stage = input("Etapa no funil: ")

    # valida os dados aqui
    # depois de validado, precisamos modelar o lead como um dict
    # para isso, usamos o model
    # agora... com meu lead modelado como um dict...
    # precisamos enviar esse leads para o leads.json
    # para isso, vamos usar o control
    control.create_leads(model_lead(name, email, stage))

    print("Lead Adicionado")

def list_leads():
    leads = control.read_leads()
    print(leads)

def main():
    while True:
        print("\n Mini CRM leads")
        print("[1] Adicionar Leads")
        print("[2] Listar Leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção Invalida")

if __name__ == "__main__":
    main()