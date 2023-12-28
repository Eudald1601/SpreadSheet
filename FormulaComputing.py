from Tokenize import Tokenize
from Parser import Parser
from GeneratePostfix import GeneratePostfix
class FormulaComputing():
    def __init__(self) -> None:
        self.tokenize = Tokenize()
        self.parse = Parser()
        self.generatePostfix = GeneratePostfix()
    
    
    def computeFormula(self, string):
        token_list = self.tokenize.tokenize(string)
        print(token_list)
        parsed_list = self.parse.parse(token_list)
        print(parsed_list)
        postfix, stack = self.generatePostfix.infixToPostfix(parsed_list)
        print(postfix, stack)
    
if __name__ == "__main__":
    formula_computing = FormulaComputing()
    formula_computing.computeFormula("A3 + B2 * (4 - SUMA(A4:B4;5))")
    