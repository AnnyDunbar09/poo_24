# Coisas para arrumar ou adicionar no código:
# Classe funcionaário
# Corrigir linha 16
# Linha 34: Caso seja adicionado uma letra ao invés de um número == ERRO ERRO ERRO
# Estudar o básico de POO
# Saber onde cada função é invocada


# Protótipo de um sistema desenvolvido para o PNAE- Fase 1

# Classe comida para representar os alimentos
class Comida:
    def __init__(self, nome, tipo_comida, data_validade, estoque):
        # Inicialização da classe Comida
        self.nome = nome
        self.tipo_comida = tipo_comida
        self.data_validade = data_validade
        self.estoque = int(estoque)  # Convertendo a quantidade de estoque para inteiro
        # Criação de um novo atributo para mostrar quanto de um alimento ainda há em estoque


# Listas para armazenar alimentos e alunos
alimentos = []
pessoas = []


# Função para registrar um novo alimento
def registrar():
    nome = input("Digite o nome do alimento a ser adicionado: ").lower()
    tipo_comida = input("Digite o tipo do alimento a ser adicionado (Industrializado ou Perecível): ").lower()
    data_validade = input("Digite a data de validade do alimento a ser adicionado: ").lower()
    estoque = int(input("Digite a quantidade do alimento a ser adicionado: ").lower())
    print("\nAlimento registrado com sucesso!")
    return Comida(nome, tipo_comida, data_validade, estoque)
    # Lower() é apenas um método para que as letras maiúsculas se transformem em minúsculas, assim o código roda de forma padronizada e sem erros.


# Função para adicionar um item ao estoque
def adicionar_item():   # Verifica se o alimento existe na lista de alimentos e permite adicionar uma quantidade específica ao estoque.
    while True:
        alimento = input("Qual alimento deseja adicionar ao estoque? R: ").lower()
        encontrado = False
        for p in alimentos:
            if alimento == p.nome:
                quantidade = int(input(f"Quantidade de {p.nome} a ser adicionada ao estoque atual.(atual: {p.estoque}): "))
                p.estoque += quantidade
                print(f"Estoque atualizado para {p.nome}: {p.estoque}")
                encontrado = True
                break
        if not encontrado:
            print("O produto procurado não está registrado no sistema!")
        continuar = input("Deseja adicionar mais algum item ao estoque? (S/N): ").upper()
        if continuar != 'S':
            break
            # upper() e lower() tem a mesma função, esses métodos padronizam os caracteres digitados.
            # lower() padroniza tudo em minúsculo e upper() padroniza tudo em maiúsculo.
            # Sabemos que para a máquina/sistema 's' e 'S' são coisas diferentes então isso é útil


# Função para remover um item do estoque
def remover_item():  # Verifica se o alimento existe na lista de alimentos e permite remover uma quantidade específica do estoque.
    while True:
        alimento = input("Qual item deseja remover do estoque? R: ").lower()
        encontrado = False
        for p in alimentos:
            if alimento == p.nome:
                quantidade = int(input(f"Quantas unidades de {p.nome} deseja remover do estoque (atual: {p.estoque}): "))
                if p.estoque < quantidade:
                    print(f"No estoque há apenas {p.estoque} unidades deste produto. Por favor, escolha uma quantidade menor!")
                else:
                    p.estoque -= quantidade
                    print(f"Você removeu {quantidade} unidades de {p.nome} do estoque!")
                    print(f"{p.nome} restante: {p.estoque}")
                encontrado = True
                break
        if not encontrado:
            print("O produto procurado não está registrado no sistema.")
        continuar = input("Deseja remover mais algum item do estoque? (S/N): ").upper()
        if continuar != 'S':
            break


# Classe Aluno para representar os alunos
class Aluno:
    def __init__(self, nome, matricula, email):
        # Inicialização da classe Aluno
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.presente = False  # Inicialmente aluno não está presente

# Método para marcar a presença do aluno
    def marcar_presenca(self):  # Pergunta ao usuário se o aluno está presente e atualiza o atributo presente de acordo.
        presenca = input("O aluno está presente (S/N): ").upper()  # upper() padroniza tudo em maiúsculo.
        if presenca == 'S':
            self.presente = True
            print(f"{self.nome} foi marcado como presente!")
        else:
            self.presente = False
            print(f"{self.nome} foi marcado como ausente!")


# Função para registrar um novo aluno
def registrar_aluno():  # Solicita informações sobre o aluno e o adiciona à lista de pessoas.
    nome_aluno = input("Qual o nome do aluno? R: ")
    matricula = input("Qual a matrícula do aluno? R: ")
    email = input("Qual o email do aluno? R: ")
    aluno = Aluno(nome_aluno, matricula, email)
    pessoas.append(aluno)   # append() é utilizado para adicionar o objeto aluno recém-criado à lista de pessoas.
    print("\nAluno registrado com sucesso!")


# Loop principal do programa
while True:
    opcoes = input("Lista de comandos:\n"
                   "(1) Alimentos em estoque.\n"
                   "(2) Alunos.\n"
                   "(0) Encerrar sessão.\n R:")
    if opcoes == '1':
        while True:
            opcoes2 = input("(1) Registrar novo alimento no estoque.\n"
                            "(2) Adicionar alimento.\n"
                            "(3) Remover alimento.\n"
                            "(4) Visualizar produtos em estoque.\n"
                            "(0) Voltar ao menu anterior.\n R:")
            if opcoes2 == '1':
                comida = registrar()
                alimentos.append(comida)
            # append() adiciona outro item ao fim da lista, isso é útil para não termos que editar a lista diretamente.
            elif opcoes2 == '2':
                adicionar_item()
            elif opcoes2 == '3':
                remover_item()
            elif opcoes2 == '4':
                for p in alimentos:
                    print(f"Produto: {p.nome}\nEstoque: {p.estoque}")
            elif opcoes2 == '0':
                break
            else:
                print("\nNão há funções para isto, por favor navegue utilizando o menu.")
    elif opcoes == '2':
        while True:
            opcoes3 = input("\n(1) Registrar aluno.\n"
                            "(2) Marcar presença do aluno.\n"
                            "(3) Visualizar lista de alunos.\n"
                            "(0) Voltar ao menu principal.\n R: ")
            if opcoes3 == '1':
                registrar_aluno()
            elif opcoes3 == '2':
                nome = input("Qual o nome do aluno: ")
                for i in pessoas:
                    if nome == i.nome:
                        i.marcar_presenca()
                        break
                else:
                    print("Este nome não está registrado no sistema! Por favor, digite outro.")
            elif opcoes3 == '3':
                print("\nLista de alunos:")
                for aluno in pessoas:
                    print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}, Email: {aluno.email}, Presente: {aluno.presente}")
            elif opcoes3 == '0':
                break
            else:
                print("Não há opções para isto! Por favor, navegue utilizando o menu.")
    elif opcoes == '0':
        break
    else:
        print("Não há opções para isto! Por favor, navegue utilizando o menu.")
