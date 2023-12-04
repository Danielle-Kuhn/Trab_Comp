class AnalisePreditiva:

    firstSet = {}  # Conjunto First
    followSet = {}  # Conjunto Follow
    tabelaAnalise = {}  # Tabela de Análise Preditiva

    @staticmethod
    def main():
        # Definindo a gramática
        AnalisePreditiva.adicionarConjuntoFirst("S", {"(", "id"})
        AnalisePreditiva.adicionarConjuntoFirst("E", {"(", "id"})
        AnalisePreditiva.adicionarConjuntoFirst("E'", {"+", "ε"})
        AnalisePreditiva.adicionarConjuntoFirst("T", {"(", "id"})
        AnalisePreditiva.adicionarConjuntoFirst("T'", {"*", "ε"})
        AnalisePreditiva.adicionarConjuntoFirst("F", {"(", "id"})

        AnalisePreditiva.adicionarConjuntoFollow("S", {"$"})
        AnalisePreditiva.adicionarConjuntoFollow("E", {"$", ")"})
        AnalisePreditiva.adicionarConjuntoFollow("E'", {"$", ")"})
        AnalisePreditiva.adicionarConjuntoFollow("T", {"$", ")", "+"})
        AnalisePreditiva.adicionarConjuntoFollow("T'", {"$", ")", "+"})
        AnalisePreditiva.adicionarConjuntoFollow("F", {"$", ")", "+", "*"})


        # Preenchendo a tabela de análise preditiva
        AnalisePreditiva.adicionarEntradaTabela("S", "(", "E$")
        AnalisePreditiva.adicionarEntradaTabela("S", "id", "E$")
        AnalisePreditiva.adicionarEntradaTabela("E", "(", "TE'")
        AnalisePreditiva.adicionarEntradaTabela("E", "id", "TE'")
        AnalisePreditiva.adicionarEntradaTabela("E'", "+", "+TE'")
        AnalisePreditiva.adicionarEntradaTabela("E'", ")", "ε")
        AnalisePreditiva.adicionarEntradaTabela("E'", "$", "ε")
        AnalisePreditiva.adicionarEntradaTabela("T", "(", "FT'")
        AnalisePreditiva.adicionarEntradaTabela("T", "id", "FT'")
        AnalisePreditiva.adicionarEntradaTabela("T'", "+", "ε")
        AnalisePreditiva.adicionarEntradaTabela("T'", "*", "*FT'")
        AnalisePreditiva.adicionarEntradaTabela("T'", ")", "ε")
        AnalisePreditiva.adicionarEntradaTabela("T'", "$", "ε")
        AnalisePreditiva.adicionarEntradaTabela("F", "(", "(E)")
        AnalisePreditiva.adicionarEntradaTabela("F", "id", "id")

        # Imprimindo a tabela de análise preditiva
        AnalisePreditiva.imprimirTabelaAnalise()

    @staticmethod
    def adicionarConjuntoFirst(simbolo, conjunto):
        AnalisePreditiva.firstSet[simbolo] = conjunto

    @staticmethod
    def adicionarConjuntoFollow(simbolo, conjunto):
        AnalisePreditiva.followSet[simbolo] = conjunto

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


# Executando o método main
AnalisePreditiva.main()
