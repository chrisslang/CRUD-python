import json

ARQUIVO_ESTUDANTES = "estudantes.json"
ARQUIVO_PROFESSORES = "professores.json"
ARQUIVO_DISCIPLINAS = "disciplinas.json"
ARQUIVO_TURMAS = "turmas.json"
ARQUIVO_MATRICULAS = "matriculas.json"

def recuperar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def apresentar_menu_principal():
    print("\nMENU PRINCIPAL")
    print("(1) Gerenciar Estudantes")
    print("(2) Gerenciar Professores")
    print("(3) Gerenciar Disciplinas")
    print("(4) Gerenciar Turmas")
    print("(5) Gerenciar Matrículas")
    print("(6) Sair")
    return input("\nSelecione a opção desejada: ")

def apresentar_menu_operacoes(entidade):
    print(f"\nMENU DE {entidade.upper()}")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Editar")
    print("(4) Excluir")
    print("(5) Voltar ao Menu Principal")
    return input("\nSelecione a operação desejada: ")

def solicitar_e_validar_codigo(dados, chave, entidade):
    while True:
        try:
            codigo = int(input(f"Digite o código do {entidade}: "))
            if any(item[chave] == codigo for item in dados):
                return codigo
            else:
                print(f"ERRO: Código de {entidade} não encontrado. Tente novamente.")
        except ValueError:
            print("Entrada inválida. O código deve ser um número inteiro.")

def solicitar_e_verificar_existencia_codigo(dados, chave):
    while True:
        try:
            codigo = int(input(f"Digite o código (somente números): "))
            if any(item[chave] == codigo for item in dados):
                print(f"ERRO: O código {codigo} já existe. Por favor, digite um novo.")
            else:
                return codigo
        except ValueError:
            print("Entrada inválida. O código deve ser um número inteiro.")


def incluir_estudante():
    print("\nINCLUIR ESTUDANTE")
    lista_de_estudantes = recuperar_dados(ARQUIVO_ESTUDANTES)
    codigo = solicitar_e_verificar_existencia_codigo(lista_de_estudantes, "codigo")
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    novo_estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    lista_de_estudantes.append(novo_estudante)
    salvar_dados(ARQUIVO_ESTUDANTES, lista_de_estudantes)
    print("Estudante incluído com sucesso!")

def listar_estudantes():
    print("\nLISTA DE ESTUDANTES")
    lista_de_estudantes = recuperar_dados(ARQUIVO_ESTUDANTES)
    if not lista_de_estudantes:
        print("Nenhum estudante cadastrado.")
    else:
        for estudante in lista_de_estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")

def editar_estudante():
    print("\nEDITAR ESTUDANTE")
    lista_de_estudantes = recuperar_dados(ARQUIVO_ESTUDANTES)
    if not lista_de_estudantes:
        print("Nenhum estudante para editar.")
        return
    try:
        codigo_editar = int(input("Digite o código do estudante que deseja editar: "))
        estudante_encontrado = next((e for e in lista_de_estudantes if e["codigo"] == codigo_editar), None)
        if estudante_encontrado:
            print(f"Editando: {estudante_encontrado['nome']}")
            novo_nome = input("Digite o NOVO nome (deixe em branco para não alterar): ")
            novo_cpf = input("Digite o NOVO CPF (deixe em branco para não alterar): ")
            if novo_nome: estudante_encontrado["nome"] = novo_nome
            if novo_cpf: estudante_encontrado["cpf"] = novo_cpf
            salvar_dados(ARQUIVO_ESTUDANTES, lista_de_estudantes)
            print("Estudante atualizado com sucesso!")
        else:
            print("Estudante não encontrado.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")

def excluir_estudante():
    print("\nEXCLUIR ESTUDANTE")
    lista_de_estudantes = recuperar_dados(ARQUIVO_ESTUDANTES)
    if not lista_de_estudantes:
        print("Nenhum estudante para excluir.")
        return
    try:
        codigo_excluir = int(input("Digite o código do estudante que deseja excluir: "))
        estudante_a_remover = next((e for e in lista_de_estudantes if e["codigo"] == codigo_excluir), None)
        if estudante_a_remover:
            lista_de_estudantes.remove(estudante_a_remover)
            salvar_dados(ARQUIVO_ESTUDANTES, lista_de_estudantes)
            print("Estudante excluído com sucesso!")
        else:
            print("Estudante não encontrado.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")

def gerenciar_estudantes():
    while True:
        operacao = apresentar_menu_operacoes("Estudantes")
        if operacao == "1": incluir_estudante()
        elif operacao == "2": listar_estudantes()
        elif operacao == "3": editar_estudante()
        elif operacao == "4": excluir_estudante()
        elif operacao == "5": break
        else: print("Opção inválida.")

def incluir_professor():
    print("\nINCLUIR PROFESSOR")
    lista = recuperar_dados(ARQUIVO_PROFESSORES)
    codigo = solicitar_e_verificar_existencia_codigo(lista, "codigo")
    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor: ")
    lista.append({"codigo": codigo, "nome": nome, "cpf": cpf})
    salvar_dados(ARQUIVO_PROFESSORES, lista)
    print("Professor incluído com sucesso!")

def listar_professores():
    print("\nLISTA DE PROFESSORES")
    lista = recuperar_dados(ARQUIVO_PROFESSORES)
    if not lista:
        print("Nenhum professor cadastrado.")
    else:
        for item in lista:
            print(f"Código: {item['codigo']}, Nome: {item['nome']}, CPF: {item['cpf']}")

def editar_professor():
    print("\nEDITAR PROFESSOR")
    lista = recuperar_dados(ARQUIVO_PROFESSORES)
    if not lista:
        print("Nenhum professor para editar.")
        return
    try:
        codigo_editar = int(input("Digite o código do professor que deseja editar: "))
        item_encontrado = next((p for p in lista if p["codigo"] == codigo_editar), None)
        if item_encontrado:
            print(f"Editando: {item_encontrado['nome']}")
            novo_nome = input("Digite o NOVO nome (deixe em branco para não alterar): ")
            novo_cpf = input("Digite o NOVO CPF (deixe em branco para não alterar): ")
            if novo_nome: item_encontrado["nome"] = novo_nome
            if novo_cpf: item_encontrado["cpf"] = novo_cpf
            salvar_dados(ARQUIVO_PROFESSORES, lista)
            print("Professor atualizado com sucesso!")
        else:
            print("Professor não encontrado.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")


def excluir_professor():
    print("\nEXCLUIR PROFESSOR")
    lista = recuperar_dados(ARQUIVO_PROFESSORES)
    if not lista:
        print("Nenhum professor para excluir.")
        return
    try:
        codigo_excluir = int(input("Digite o código do professor que deseja excluir: "))
        item_a_remover = next((p for p in lista if p["codigo"] == codigo_excluir), None)
        if item_a_remover:
            lista.remove(item_a_remover)
            salvar_dados(ARQUIVO_PROFESSORES, lista)
            print("Professor excluído com sucesso!")
        else:
            print("Professor não encontrado.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")

def gerenciar_professores():
    while True:
        operacao = apresentar_menu_operacoes("Professores")
        if operacao == "1": incluir_professor()
        elif operacao == "2": listar_professores()
        elif operacao == "3": editar_professor()
        elif operacao == "4": excluir_professor()
        elif operacao == "5": break
        else: print("Opção inválida.")

def incluir_disciplina():
    print("\nINCLUIR DISCIPLINA")
    lista = recuperar_dados(ARQUIVO_DISCIPLINAS)
    codigo = solicitar_e_verificar_existencia_codigo(lista, "codigo")
    nome = input("Digite o nome da disciplina: ")
    lista.append({"codigo": codigo, "nome": nome})
    salvar_dados(ARQUIVO_DISCIPLINAS, lista)
    print("Disciplina incluída com sucesso!")

def listar_disciplinas():
    print("\nLISTA DE DISCIPLINAS")
    lista = recuperar_dados(ARQUIVO_DISCIPLINAS)
    if not lista:
        print("Nenhuma disciplina cadastrada.")
    else:
        for item in lista:
            print(f"Código: {item['codigo']}, Nome: {item['nome']}")

def editar_disciplina():
    print("\nEDITAR DISCIPLINA")
    lista = recuperar_dados(ARQUIVO_DISCIPLINAS)
    if not lista:
        print("Nenhuma disciplina para editar.")
        return
    try:
        codigo_editar = int(input("Digite o código da disciplina que deseja editar: "))
        item_encontrado = next((d for d in lista if d["codigo"] == codigo_editar), None)
        if item_encontrado:
            print(f"Editando: {item_encontrado['nome']}")
            novo_nome = input("Digite o NOVO nome (deixe em branco para não alterar): ")
            if novo_nome: item_encontrado["nome"] = novo_nome
            salvar_dados(ARQUIVO_DISCIPLINAS, lista)
            print("Disciplina atualizada com sucesso!")
        else:
            print("Disciplina não encontrada.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")

def excluir_disciplina():
    print("\nEXCLUIR DISCIPLINA")
    lista = recuperar_dados(ARQUIVO_DISCIPLINAS)
    if not lista:
        print("Nenhuma disciplina para excluir.")
        return
    try:
        codigo_excluir = int(input("Digite o código da disciplina que deseja excluir: "))
        item_a_remover = next((d for d in lista if d["codigo"] == codigo_excluir), None)
        if item_a_remover:
            lista.remove(item_a_remover)
            salvar_dados(ARQUIVO_DISCIPLINAS, lista)
            print("Disciplina excluída com sucesso!")
        else:
            print("Disciplina não encontrada.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")

def gerenciar_disciplinas():
    while True:
        operacao = apresentar_menu_operacoes("Disciplinas")
        if operacao == "1": incluir_disciplina()
        elif operacao == "2": listar_disciplinas()
        elif operacao == "3": editar_disciplina()
        elif operacao == "4": excluir_disciplina()
        elif operacao == "5": break
        else: print("Opção inválida.")

def incluir_turma():
    print("\nINCLUIR TURMA")
    turmas = recuperar_dados(ARQUIVO_TURMAS)
    professores = recuperar_dados(ARQUIVO_PROFESSORES)
    disciplinas = recuperar_dados(ARQUIVO_DISCIPLINAS)

    if not professores or not disciplinas:
        print("ERRO: É necessário ter ao menos um professor e uma disciplina cadastrados.")
        return

    codigo_turma = solicitar_e_verificar_existencia_codigo(turmas, "codigo_turma")
    
    print("--- Professores Disponíveis ---")
    listar_professores()
    codigo_professor = solicitar_e_validar_codigo(professores, "codigo", "professor")
    
    print("--- Disciplinas Disponíveis ---")
    listar_disciplinas()
    codigo_disciplina = solicitar_e_validar_codigo(disciplinas, "codigo", "disciplina")

    turmas.append({
        "codigo_turma": codigo_turma,
        "codigo_professor": codigo_professor,
        "codigo_disciplina": codigo_disciplina
    })
    salvar_dados(ARQUIVO_TURMAS, turmas)
    print("Turma incluída com sucesso!")

def listar_turmas():
    print("\nLISTA DE TURMAS")
    turmas = recuperar_dados(ARQUIVO_TURMAS)
    if not turmas:
        print("Nenhuma turma cadastrada.")
    else:
        professores = recuperar_dados(ARQUIVO_PROFESSORES)
        disciplinas = recuperar_dados(ARQUIVO_DISCIPLINAS)
        for turma in turmas:
            prof = next((p['nome'] for p in professores if p['codigo'] == turma['codigo_professor']), "Não encontrado")
            disc = next((d['nome'] for d in disciplinas if d['codigo'] == turma['codigo_disciplina']), "Não encontrada")
            print(f"Cód. Turma: {turma['codigo_turma']}, Professor: {prof} (Cód: {turma['codigo_professor']}), Disciplina: {disc} (Cód: {turma['codigo_disciplina']})")


def editar_turma():
    print("\nEDITAR TURMA")
    turmas = recuperar_dados(ARQUIVO_TURMAS)
    if not turmas:
        print("Nenhuma turma para editar.")
        return
    try:
        codigo_editar = int(input("Digite o código da turma que deseja editar: "))
        turma_encontrada = next((t for t in turmas if t["codigo_turma"] == codigo_editar), None)
        if turma_encontrada:
            professores = recuperar_dados(ARQUIVO_PROFESSORES)
            disciplinas = recuperar_dados(ARQUIVO_DISCIPLINAS)

            print("--- Editando Turma ---")
            print(f"Professor atual: {turma_encontrada['codigo_professor']}")
            if input("Deseja alterar o professor? (s/n): ").lower() == 's':
                listar_professores()
                turma_encontrada['codigo_professor'] = solicitar_e_validar_codigo(professores, "codigo", "professor")
            
            print(f"Disciplina atual: {turma_encontrada['codigo_disciplina']}")
            if input("Deseja alterar a disciplina? (s/n): ").lower() == 's':
                listar_disciplinas()
                turma_encontrada['codigo_disciplina'] = solicitar_e_validar_codigo(disciplinas, "codigo", "disciplina")
            
            salvar_dados(ARQUIVO_TURMAS, turmas)
            print("Turma atualizada com sucesso!")
        else:
            print("Turma não encontrada.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")


def excluir_turma():
    print("\nEXCLUIR TURMA")
    turmas = recuperar_dados(ARQUIVO_TURMAS)
    if not turmas:
        print("Nenhuma turma para excluir.")
        return
    try:
        codigo_excluir = int(input("Digite o código da turma que deseja excluir: "))
        item_a_remover = next((t for t in turmas if t["codigo_turma"] == codigo_excluir), None)
        if item_a_remover:
            turmas.remove(item_a_remover)
            salvar_dados(ARQUIVO_TURMAS, turmas)
            print("Turma excluída com sucesso!")
        else:
            print("Turma não encontrada.")
    except ValueError:
        print("Entrada inválida. O código deve ser um número.")

def gerenciar_turmas():
    while True:
        operacao = apresentar_menu_operacoes("Turmas")
        if operacao == "1": incluir_turma()
        elif operacao == "2": listar_turmas()
        elif operacao == "3": editar_turma()
        elif operacao == "4": excluir_turma()
        elif operacao == "5": break
        else: print("Opção inválida.")

def incluir_matricula():
    print("\nINCLUIR MATRÍCULA")
    matriculas = recuperar_dados(ARQUIVO_MATRICULAS)
    turmas = recuperar_dados(ARQUIVO_TURMAS)
    estudantes = recuperar_dados(ARQUIVO_ESTUDANTES)

    if not turmas or not estudantes:
        print("ERRO: É necessário ter ao menos uma turma e um estudante cadastrados.")
        return
    
    print("--- Turmas Disponíveis ---")
    listar_turmas()
    codigo_turma = solicitar_e_validar_codigo(turmas, "codigo_turma", "turma")
    
    print("--- Estudantes Disponíveis ---")
    listar_estudantes()
    codigo_estudante = solicitar_e_validar_codigo(estudantes, "codigo", "estudante")

    if any(m['codigo_turma'] == codigo_turma and m['codigo_estudante'] == codigo_estudante for m in matriculas):
        print("ERRO: Este estudante já está matriculado nesta turma.")
        return

    matriculas.append({"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante})
    salvar_dados(ARQUIVO_MATRICULAS, matriculas)
    print("Matrícula realizada com sucesso!")

def listar_matriculas():
    print("\nLISTA DE MATRÍCULAS")
    matriculas = recuperar_dados(ARQUIVO_MATRICULAS)
    if not matriculas:
        print("Nenhuma matrícula cadastrada.")
    else:
        estudantes = recuperar_dados(ARQUIVO_ESTUDANTES)
        turmas = recuperar_dados(ARQUIVO_TURMAS)
        disciplinas = recuperar_dados(ARQUIVO_DISCIPLINAS)

        for matricula in matriculas:
            turma_info = next((t for t in turmas if t['codigo_turma'] == matricula['codigo_turma']), None)
            estudante_nome = next((e['nome'] for e in estudantes if e['codigo'] == matricula['codigo_estudante']), "Não encontrado")
            
            if turma_info:
                disciplina_nome = next((d['nome'] for d in disciplinas if d['codigo'] == turma_info['codigo_disciplina']), "Não encontrada")
                print(f"Turma: {turma_info['codigo_turma']} ({disciplina_nome}) - Estudante: {estudante_nome} (Cód: {matricula['codigo_estudante']})")
            else:
                 print(f"Turma: {matricula['codigo_turma']} (inválida) - Estudante: {estudante_nome} (Cód: {matricula['codigo_estudante']})")

def editar_matricula():
    print("\nA funcionalidade de editar matrícula não está implementada.")

def excluir_matricula():
    print("\nEXCLUIR MATRÍCULA")
    matriculas = recuperar_dados(ARQUIVO_MATRICULAS)
    if not matriculas:
        print("Nenhuma matrícula para excluir.")
        return
    
    try:
        listar_matriculas()
        codigo_turma = int(input("Digite o código da TURMA da matrícula a ser excluída: "))
        codigo_estudante = int(input("Digite o código do ESTUDANTE da matrícula a ser excluída: "))
        
        matricula_a_remover = next((m for m in matriculas if m['codigo_turma'] == codigo_turma and m['codigo_estudante'] == codigo_estudante), None)
        
        if matricula_a_remover:
            matriculas.remove(matricula_a_remover)
            salvar_dados(ARQUIVO_MATRICULAS, matriculas)
            print("Matrícula excluída com sucesso!")
        else:
            print("Matrícula não encontrada.")
    except ValueError:
        print("Entrada inválida. Os códigos devem ser números.")

def gerenciar_matriculas():
    while True:
        operacao = apresentar_menu_operacoes("Matrículas")
        if operacao == "1": incluir_matricula()
        elif operacao == "2": listar_matriculas()
        elif operacao == "3": editar_matricula()
        elif operacao == "4": excluir_matricula()
        elif operacao == "5": break
        else: print("Opção inválida.")

while True:
    escolha = apresentar_menu_principal()

    if escolha == "1": gerenciar_estudantes()
    elif escolha == "2": gerenciar_professores()
    elif escolha == "3": gerenciar_disciplinas()
    elif escolha == "4": gerenciar_turmas()
    elif escolha == "5": gerenciar_matriculas()
    elif escolha == "6":
        print("Até mais, usuário(a)!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")