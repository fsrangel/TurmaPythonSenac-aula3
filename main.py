from biblioteca import Biblioteca
import menu
import adicionar
import exibir
import pesquisar
import marcar_emprestado
import remover

def main():
    biblioteca = Biblioteca()

    while True:
        escolha = menu.exibir_menu()
        if escolha == '1':
            adicionar.adicionar_livro(biblioteca)
        elif escolha == '2':
            exibir.exibir_livros(biblioteca)
        elif escolha == '3':
            pesquisar.pesquisar_livros(biblioteca)
        elif escolha == '4':
            marcar_emprestado.marcar_emprestado(biblioteca)
        elif escolha == '5':
            remover.remover_livro(biblioteca)
        elif escolha == '6':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
