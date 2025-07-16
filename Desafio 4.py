def adicionar_contato(nome, telefone, email):
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    return contato

def visualizar_contatos(contatos):
    if not contatos:
        print("Nenhum contato encontrado.")
        return

    print("Lista de Contatos:")
    for contato in contatos:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

def buscar_contato(nome, contatos):
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            return contato
    return None

def remover_contato(nome, contatos):
    for i, contato in enumerate(contatos):
        if contato['nome'].lower() == nome.lower():
            del contatos[i]
            print(f"Contato {nome} removido com sucesso!")
            return True
    print(f"Contato {nome} não encontrado.")
    return False

if __name__ == "__main__":
    contatos = []
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")


        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            novo_contato = adicionar_contato(nome, telefone, email)
            contatos.append(novo_contato)
        elif opcao == '2':
            visualizar_contatos(contatos)
        elif opcao == '3':
            nome_busca = input("Digite o nome do contato que deseja buscar: ")
            contato_encontrado = buscar_contato(nome_busca, contatos)
            if contato_encontrado:
                print(f"Contato encontrado: Nome: {contato_encontrado['nome']}, Telefone: {contato_encontrado['telefone']}, Email: {contato_encontrado['email']}")
            else:
                print(f"Contato '{nome_busca}' não encontrado.")
        elif opcao == '4':
            nome_remover = input("Digite o nome do contato que deseja remover: ")
            remover_contato(nome_remover, contatos)
        elif opcao == '5':
            print("Saindo do Gerenciador de Contatos. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")
