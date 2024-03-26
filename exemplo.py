class Usuario:
    def __init__(self, nome, cpf, email, livros=[]):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.livros_emprestados = livros

class Livro:
    def __init__(self, titulo, genero, editora, author, exemplares, qtd=0):
        self.titulo = titulo
        self.genero = genero
        self.editora = editora
        self.autor = author
        self.num_exemplares = exemplares
        self.qtd_emprestados = qtd

    def emprestar(self):
        if self.num_exemplares > self.qtd_emprestados:
            self.qtd_emprestados -= 1
            return True
        else:
            return False

    def devolver(self):
        if self.qtd_emprestados > 0 and (self.qtd_emprestados <= self.num_exemplares):
            self.qtd_emprestados += 1
            return True
        else:
            return False


novo_usuario1 = Usuario("Vitor", "987654", "vitorvilasboas@ifto.edu.br")
novo_usuario2 = Usuario("Maria", "897526", "maria@ifto.edu.br")
novo_usuario3 = Usuario("Pedro", "568712", "pedro@gmail.com")
novo_usuario4 = Usuario("Kamyla", "123456", "kamyla.sousa@estudante.ifto.edu.br")

# print(novo_usuario4.nome, novo_usuario4.cpf, novo_usuario4.email, novo_usuario4.livros_emprestados)
# novo_usuario4.cpf = "999999999"
# print(novo_usuario4.nome, novo_usuario4.cpf)
# # print(novo_usuario2.livros_emprestados, novo_usuario1.livros_emprestados)

novo_livro1 = Livro("Dom Casmurro", "Literatura", "Erika", "Machado de Assis", 10)
novo_livro2 = Livro("Memórias Póstumas de Bráz Cubas", "Comédia", "Universal", "Cecilia Meireles", 2)
novo_livro3 = Livro("Mundo Novo", "Suspense", "Elsevier", "Fulano de tal", 5)

# print("Genero Livro 2:", novo_livro2.genero, "\n", "Titulo livro 1: ", novo_livro1.titulo)
#
# novo_livro2.genero = "Terror"
#
# print("Genero Livro 2:", novo_livro2.genero)


print(novo_usuario1.livros_emprestados)


if novo_livro1.emprestar():
    novo_usuario1.livros_emprestados.append(novo_livro1)

print(novo_usuario1.livros_emprestados[0].genero)


novo_usuario2.livros_emprestados.append(novo_livro3)
novo_usuario2.livros_emprestados.append(novo_livro2)

print(novo_usuario2.livros_emprestados[1].autor)






