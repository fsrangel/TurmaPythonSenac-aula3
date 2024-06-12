def exibir_livros(biblioteca):
    if not biblioteca.livros:
        print("Nenhum livro cadastrado.")
    else:
        biblioteca.exibir_livros()
