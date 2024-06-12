def pesquisar_livros(biblioteca):
    chave = input("Pesquisar por (titulo/autor): ").lower()
    if chave in ['titulo', 'autor']:
        valor = input(f"Digite o {chave}: ")
        resultados = biblioteca.pesquisar_livros(chave, valor)
        if resultados:
            for livro in resultados:
                print(livro)
        else:
            print("Nenhum livro encontrado.")
    else:
        print("Opção inválida.")
