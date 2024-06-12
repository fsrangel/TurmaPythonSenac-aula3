from biblioteca import Livro

def adicionar_livro(biblioteca):
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    livro = Livro(titulo, autor, ano)
    biblioteca.adicionar_livro(livro)
    print("Livro adicionado com sucesso!")
