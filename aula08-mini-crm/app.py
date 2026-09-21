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
    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]: <12} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()

    search_results = control.read_leads_search(query)
    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]: <12} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()
    if path_csv is None:
        print("Não foi possivel exportar para CSV")
    else:
        print(f"Exportado para CSV {path_csv}")

def main():
    while True:
        print("\n Mini CRM leads")
        print("[1] Adicionar Leads")
        print("[2] Listar Leads")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar Para CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        else:
            print("Opção Invalida")

if __name__ == "__main__":
    main()