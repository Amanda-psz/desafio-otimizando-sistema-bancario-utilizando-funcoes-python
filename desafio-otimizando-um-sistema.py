def menu():
    menu = """\n
    ================== MENU ==================
    
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar Contas
    [0] Sair

    => """
    return(input(menu))

def depositar(saldo, valor_depositado, extrato, /):
    
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f"Déposito:\t\tR$ {valor_depositado:.2f}\n"
        print("\nDepósito realizado com sucesso!")

    else:
        print("Falha na operação! O valor informado é inválido.")

    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
        
    if excedeu_saldo:
        print("Falha na operação! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Falha na operação! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Falha na operação! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Falha na operação! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *,extrato):

    print("\n===================== Extrato =====================")
    print("Não foram realizado movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("=====================================================")

def criar_usuario(usuarios):
    
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logragradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):

    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            Número da conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 80)
        print(linha)


def iniciar():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "1":
            valor_depositado = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor_depositado, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


iniciar()
