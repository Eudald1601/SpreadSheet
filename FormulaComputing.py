from Tokenize import Tokenize

class FormulaComputing():
    def __init__(self) -> None:
        self.tokenize = Tokenize()
        pass
    
    
if __name__ == "__main__":
    tokenize= Tokenize()
    lista = tokenize.tokenize("=4 + A4 / PROMEDIO(A4:B4)")
    print(lista)