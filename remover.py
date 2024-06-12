def remover_livro(biblioteca):
    titulo = input("Título do livro a ser removido: ")
    if biblioteca.remover_livro(titulo):
        print("Livro removido com sucesso.")
    else:
        print("Livro não encontrado.")
