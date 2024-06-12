class Livro:
    def __init__(self, titulo, autor, ano, status='disponível'):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.ano}) - {self.status}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_livros(self):
        for livro in self.livros:
            print(livro)

    def pesquisar_livros(self, chave, valor):
        resultados = [livro for livro in self.livros if getattr(livro, chave) == valor]
        return resultados

    def marcar_emprestado(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.status = 'emprestado'
                return True
        return False

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                return True
        return False
