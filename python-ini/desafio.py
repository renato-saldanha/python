LIMITE_SAQUES = 3
VALOR_LIMITE = 500

class Conta:
    def __init__(self, numero_conta=int, saldo=float, extrato=str, numero_saques=int):
        self.numero_conta = numero_conta
        self.agencia = "0001"
        self.saldo = saldo
        self.limite = VALOR_LIMITE
        self.extrato = extrato
        self.numero_saques = int = numero_saques

class Usuario:
    def __init__(self, nome=str, data_nascimento=str, cpf=str, endereco=str, contas=[Conta]):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = contas

def depositar(p_saldo, p_extrato, p_numero_saques, p_usuario, indice_conta):
    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
        contas_atualizada = p_usuario.contas 
        contas_atualizada[indice_conta] = Conta(
            numero_conta = p_usuario.contas[indice_conta].numero_conta,
            saldo = p_saldo + valor,
            extrato = p_extrato +  f"Depósito: R$ {valor:.2f}\n",
            numero_saques = p_numero_saques
        )
        
        usuario =  Usuario(
            nome = p_usuario.nome,
            contas = contas_atualizada,
        )
        
        print(f"""
        Saldo:{usuario.contas[indice_conta].saldo}""")
        
        return usuario
    else:
        print("Operação falhou! O valor informado é inválido.")
        
        return Usuario(
            saldo = p_saldo,
            extrato = p_extrato,
            numero_saques = p_numero_saques
        )
        
def sacar(*, p_saldo, p_limite, p_numero_saques, p_extrato, p_usuario, p_indice_conta_selecionada):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > p_saldo

    excedeu_limite = valor > p_limite

    excedeu_saques = p_numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return p_usuario

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return p_usuario

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return p_usuario

    elif valor > 0:
        contas_atualizada = p_usuario.contas 
        contas_atualizada[p_indice_conta_selecionada] = Conta(
            numero_conta = p_usuario.contas[p_indice_conta_selecionada].numero_conta,
            saldo = p_saldo - valor,
            extrato = p_extrato + f"Saque: R$ {valor:.2f}\n",
            numero_saques = p_numero_saques + 1
        )
        
        usuario =  Usuario(
            nome = p_usuario.nome,
            contas = contas_atualizada,
        )
        
        print(f"""
        Saldo:{usuario.contas[p_indice_conta_selecionada].saldo}""")
        
        return usuario
    else:
        print("Operação falhou! O valor informado é inválido.")
        
        return p_usuario
        
def ver_extrato(saldo, *, p_extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not p_extrato else p_extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def criar_conta(usuario=Usuario):
    numero_conta = len(usuario.contas) + 1    
    
    nova_conta = Conta(numero_conta=numero_conta,
                       saldo = 0,
                       extrato = "",
                       numero_saques = 0)  
    return nova_conta
    
def criar_usuario(lista_usuarios=[Usuario]):
    nome = ""
    data_nascimento = ""
    cpf_valido = False
    logradouro = ""
    numero = ""
    bairro = ""
    cidade = ""
    sigla_uf = ""
    
    while not nome:
        nome = input("""Digite o nome do novo usuário:
    => """ )
     
    while not data_nascimento:    
        data_nascimento = input("""Digite a data de nascimento(DD/MM/AAA):
    => """ )
        
    msg_cpf = """Digite um CPF válido:        
    => """    
        
    while not cpf_valido:  
        cpf = input(msg_cpf)
        cpf_sem_caracteres = cpf.replace(".", "").replace("-", "")
        
        cpf_nao_existe = all(usuario.cpf != cpf_sem_caracteres for usuario in lista_usuarios)
        if not cpf_nao_existe:
            msg_cpf = """CPF já cadastrado, favor digitar um outro CPF válido:        
    => """ 
        cpf_valido = len(cpf_sem_caracteres) == 11 and all(caractere.isdigit() for caractere in cpf_sem_caracteres) and cpf_nao_existe
        
    while not logradouro: 
        logradouro = input("""Digite o logradouro:
    => """ )
    
    while not numero: 
        numero = input("""Digite o número do logradouro:
    => """ )
    
    while not bairro: 
        bairro = input("""Digite o bairro:
    => """ )
    
    while not cidade: 
        cidade = input("""Digite a cidade:
    => """ )
    
    while not sigla_uf: 
        sigla_uf = input("""Digite a sigla do estado:
    => """ )
    
    endereco = f"Rua: {logradouro}, Nº {numero}, Bairro: {bairro} - Cidade: {cidade}/{sigla_uf.upper()}"
    return Usuario(
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            endereco=endereco,
            contas= []
    )
        
def acessar_banco():
    usuario_selecionado = Usuario
    
    def msg_conta_selecionada(contas=[Conta]):
        opcoes = "\n".join(
            f"""
        [{indice}] Conta {conta.numero_conta}"""
            for indice, conta in enumerate(contas, start=1)
        )
        return f"""Favor selecionar uma conta da lista: {opcoes}
    => """
    def msg_usuario_selecionado(lista_usuarios=[Usuario]):
        opcoes = "\n".join(
            f"""
        [{indice}] Usuário {usuario.nome}"""
            for indice, usuario in enumerate(lista_usuarios, start=1)
        )
        return f"""Favor selecionar uma usuário da lista: {opcoes}
    => """
    
    msg_opcao_inicial = """Não há usuário cadastrado, deseja cadastrar? [s]/[n] 
    => """
    msg_opcao_primeira_conta = """Não existe conta cadastrada, deseja criar uma conta? [s]/[n]
    => """
    msg_opcao_menu_conta="""
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [v] Voltar
        [q] Sair

    => """
    msg_opcao_nova_conta = """Conta criada, deseja criar outra? [s]/[n]
    => """
    msg_opcao_criar_conta = """Deseja criar uma conta? [s]/[n]
    => """
    
    lista_usuarios = [Usuario("", "", "", "", [])]
    
    opcao_inicial = input(msg_opcao_inicial)
    opcao_nova_conta = ""
    
    usuario = lista_usuarios[0]
    
    conta = Conta
    
    while opcao_inicial == "s":        
        indice_usuario_selecionado = -1
        
        if not usuario.nome:            
            usuario = criar_usuario(lista_usuarios)            
        if not usuario.contas:
            opcao_primeira_conta = input(msg_opcao_primeira_conta)
            
            if opcao_primeira_conta == "n":
                return
            
            conta = criar_conta(usuario)  
            usuario.contas.append(conta)
            lista_usuarios.pop()
            lista_usuarios.append(usuario)
        else:
            opcao_criar_conta = input(msg_opcao_criar_conta)
            
            if opcao_primeira_conta == "n":
                return
            
            if opcao_criar_conta == "s":
                conta = criar_conta(usuario) 
                lista_usuarios[indice_usuario_selecionado].contas.append(conta)  
            
        while opcao_nova_conta != "n":
            opcao_nova_conta = input(msg_opcao_nova_conta)
            
            if opcao_nova_conta == "s":
                conta = criar_conta(usuario)
                lista_usuarios[indice_usuario_selecionado].contas.extend([conta])  
                
        indice_usuario = {int(indice): len(usuario.contas) for indice, usuario in enumerate(lista_usuarios, start=0)}
        acessar_usuario = False
        
        while indice_usuario_selecionado not in indice_usuario:
            indice_usuario_selecionado = int(input(msg_usuario_selecionado(lista_usuarios))) - 1
            if indice_usuario_selecionado in indice_usuario:
                acessar_usuario = True
                usuario_selecionado = lista_usuarios[indice_usuario_selecionado]        
                
        indice_conta_selecionada = -1
        acessar_conta = False
        
        indice_contas = {int(indice): conta.numero_conta for indice, conta in enumerate(usuario.contas, start=0)}
        while indice_conta_selecionada not in indice_contas:
            indice_conta_selecionada = int(input(msg_conta_selecionada(usuario_selecionado.contas))) - 1
            if indice_conta_selecionada in indice_contas:
                acessar_conta = True
            
        while acessar_conta:
            opcao_menu_conta = input(msg_opcao_menu_conta)

            if opcao_menu_conta == "d":
                usuario = depositar(usuario_selecionado.contas[indice_conta_selecionada].saldo,
                                    usuario_selecionado.contas[indice_conta_selecionada].extrato,
                                    usuario_selecionado.contas[indice_conta_selecionada].numero_saques,
                                    usuario_selecionado,
                                    indice_conta_selecionada)
            elif opcao_menu_conta == "s":
                usuario = sacar(p_saldo = usuario_selecionado.contas[indice_conta_selecionada].saldo,
                                p_limite = usuario_selecionado.contas[indice_conta_selecionada].limite,
                                p_extrato = usuario_selecionado.contas[indice_conta_selecionada].extrato,
                                p_numero_saques = usuario_selecionado.contas[indice_conta_selecionada].numero_saques,
                                p_usuario = usuario_selecionado,
                                p_indice_conta_selecionada = indice_conta_selecionada)
            elif opcao_menu_conta == "e":
                ver_extrato(usuario_selecionado.contas[indice_conta_selecionada].saldo,
                            p_extrato = usuario_selecionado.contas[indice_conta_selecionada].extrato)
            elif opcao_menu_conta == "v":
                indice_conta_selecionada = ""
                acessar_conta = False
                opcao_nova_conta = "n"
            elif opcao_menu_conta == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
        #if opcao_inicial == "n":
            
    
    

    
            
acessar_banco()