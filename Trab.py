class AnalisePreditiva:

    primeiroConjunto = {}  # Conjunto First
    seguindoConjunto = {}  # Conjunto Follow
    tabelaAnalise = {}  # Tabela de Análise Preditiva

    @staticmethod
    def principal():
        # Definindo a gramática
        AnalisePreditiva.adicionarConjuntoFirst("S", {"(", "id"})
        AnalisePreditiva.adicionarConjuntoFirst("A", {"(", "id"})
        AnalisePreditiva.adicionarConjuntoFirst("B", {"+", "ε"})
        AnalisePreditiva.adicionarConjuntoFirst("C", {"(", "id"})
        AnalisePreditiva.adicionarConjuntoFirst("D", {"*", "ε"})
        AnalisePreditiva.adicionarConjuntoFirst("E", {"(", "id"})

        AnalisePreditiva.adicionarConjuntoFollow("S", {"$"})
        AnalisePreditiva.adicionarConjuntoFollow("A", {"$", ")"})
        AnalisePreditiva.adicionarConjuntoFollow("B", {"$", ")"})
        AnalisePreditiva.adicionarConjuntoFollow("C", {"$", ")", "+"})
        AnalisePreditiva.adicionarConjuntoFollow("D", {"$", ")", "+"})
        AnalisePreditiva.adicionarConjuntoFollow("E", {"$", ")", "+", "*"})


        # Preenchendo a tabela de análise preditiva
        AnalisePreditiva.adicionarEntradaTabela("S", "(", "AE$")
        AnalisePreditiva.adicionarEntradaTabela("S", "id", "AE$")
        AnalisePreditiva.adicionarEntradaTabela("A", "(", "CBE'")
        AnalisePreditiva.adicionarEntradaTabela("A", "id", "CBE'")
        AnalisePreditiva.adicionarEntradaTabela("B", "+", "+CBE'")
        AnalisePreditiva.adicionarEntradaTabela("B", ")", "ε")
        AnalisePreditiva.adicionarEntradaTabela("B", "$", "ε")
        AnalisePreditiva.adicionarEntradaTabela("C", "(", "DE'")
        AnalisePreditiva.adicionarEntradaTabela("C", "id", "DE'")
        AnalisePreditiva.adicionarEntradaTabela("D", "+", "ε")
        AnalisePreditiva.adicionarEntradaTabela("D", "*", "*DE'")
        AnalisePreditiva.adicionarEntradaTabela("D", ")", "ε")
        AnalisePreditiva.adicionarEntradaTabela("D", "$", "ε")
        AnalisePreditiva.adicionarEntradaTabela("E", "(", "(C)")
        AnalisePreditiva.adicionarEntradaTabela("E", "id", "id")

        # Imprimindo a tabela de análise preditiva
        AnalisePreditiva.imprimirTabelaAnalise()

    @staticmethod
    def adicionarConjuntoFirst(simbolo, conjunto):
        AnalisePreditiva.primeiroConjunto[simbolo] = conjunto

    @staticmethod
    def adicionarConjuntoFollow(simbolo, conjunto):
        AnalisePreditiva.seguindoConjunto[simbolo] = conjunto

    @staticmethod
    def adicionarEntradaTabela(naoTerminal, terminal, producao):
        if naoTerminal not in AnalisePreditiva.tabelaAnalise:
            AnalisePreditiva.tabelaAnalise[naoTerminal] = {}
        AnalisePreditiva.tabelaAnalise[naoTerminal][terminal] = producao

    @staticmethod
    def imprimirTabelaAnalise():
        print("Tabela de Análise Preditiva:")
        print("\t", end="")
        for terminal in {"(", "id", "+", "*", ")", "$"}:
            print(terminal + "\t", end="")
        print()
        for naoTerminal, linha in AnalisePreditiva.tabelaAnalise.items():
            print(naoTerminal + "\t", end="")
            for terminal in {"(", "id", "+", "*", ")", "$"}:
                if terminal in linha:
                    print(linha[terminal] + "\t", end="")
                else:
                    print("-\t", end="")
            print()

# Executando o método principal
AnalisePreditiva.principal()
