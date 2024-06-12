def marcar_emprestado(biblioteca):
    titulo = input("Título do livro a ser marcado como emprestado: ")
    if biblioteca.marcar_emprestado(titulo):
        print("Livro marcado como emprestado.")
    else:
        print("Livro não encontrado.")
