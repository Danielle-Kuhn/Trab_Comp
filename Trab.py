class AnalisePreditiva:
    # Constantes para terminais
    OPEN_PAREN = "("
    ID = "id"
    PLUS = "+"
    STAR = "*"
    CLOSE_PAREN = ")"
    EOF = "$"

    def __init__(self):
        self.primeiro_conjunto = {}
        self.segundo_conjunto = {}
        self.tabela_analise = {}

    def principal(self):
        self.definir_gramatica()
        self.preencher_tabela_analise()
        self.imprimir_tabela_analise()

    def definir_gramatica(self):
        # Definição da gramática
        self.adicionar_conjunto_first("S", {self.OPEN_PAREN, self.ID})
        self.adicionar_conjunto_first("A", {self.OPEN_PAREN, self.ID})
        self.adicionar_conjunto_first("B", {self.PLUS, "ε"})
        self.adicionar_conjunto_first("C", {self.OPEN_PAREN, self.ID})
        self.adicionar_conjunto_first("D", {self.STAR, "ε"})
        self.adicionar_conjunto_first("E", {self.OPEN_PAREN, self.ID})

        self.adicionar_conjunto_follow("S", {self.EOF})
        self.adicionar_conjunto_follow("A", {self.EOF, self.CLOSE_PAREN})
        self.adicionar_conjunto_follow("B", {self.EOF, self.CLOSE_PAREN})
        self.adicionar_conjunto_follow("C", {self.EOF, self.CLOSE_PAREN, self.PLUS})
        self.adicionar_conjunto_follow("D", {self.EOF, self.CLOSE_PAREN, self.PLUS})
        self.adicionar_conjunto_follow("E", {self.EOF, self.CLOSE_PAREN, self.PLUS, self.STAR})

    def preencher_tabela_analise(self):
        self.adicionar_entrada_tabela("S", self.OPEN_PAREN, "AE$")
        self.adicionar_entrada_tabela("S", self.ID, "AE$")
        self.adicionar_entrada_tabela("A", self.OPEN_PAREN, "CBE'")
        self.adicionar_entrada_tabela("A", self.ID, "CBE'")
        self.adicionar_entrada_tabela("B", self.PLUS, "+CBE'")
        self.adicionar_entrada_tabela("B", self.CLOSE_PAREN, "ε")
        self.adicionar_entrada_tabela("B", self.EOF, "ε")
        self.adicionar_entrada_tabela("C", self.OPEN_PAREN, "DE'")
        self.adicionar_entrada_tabela("C", self.ID, "DE'")
        self.adicionar_entrada_tabela("D", self.PLUS, "ε")
        self.adicionar_entrada_tabela("D", self.STAR, "*DE'")
        self.adicionar_entrada_tabela("D", self.CLOSE_PAREN, "ε")
        self.adicionar_entrada_tabela("D", self.EOF, "ε")
        self.adicionar_entrada_tabela("E", self.OPEN_PAREN, "(C)")
        self.adicionar_entrada_tabela("E", self.ID, "id")

    def adicionar_conjunto_first(self, simbolo, conjunto):
        self.primeiro_conjunto[simbolo] = conjunto

    def adicionar_conjunto_follow(self, simbolo, conjunto):
        self.segundo_conjunto[simbolo] = conjunto

    def adicionar_entrada_tabela(self, nao_terminal, terminal, producao):
        if nao_terminal not in self.tabela_analise:
            self.tabela_analise[nao_terminal] = {}
        self.tabela_analise[nao_terminal][terminal] = producao

    def imprimir_tabela_analise(self):
        print("Tabela de Análise Preditiva:")
        print("\t", end="")
        for terminal in {self.OPEN_PAREN, self.ID, self.PLUS, self.STAR, self.CLOSE_PAREN, self.EOF}:
            print(terminal + "\t", end="")
        print()
        for nao_terminal, linha in self.tabela_analise.items():
            print(nao_terminal + "\t", end="")
            for terminal in {self.OPEN_PAREN, self.ID, self.PLUS, self.STAR, self.CLOSE_PAREN, self.EOF}:
                if terminal in linha:
                    print(linha[terminal] + "\t", end="")
                else:
                    print("-\t", end="")
            print()

# Criando uma instância da classe e executando o método principal
analise = AnalisePreditiva()
analise.principal()
