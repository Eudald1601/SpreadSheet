from .Tokenize import Tokenize
from .Parser import Parser
from .GeneratePostfix import GeneratePostfix
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
        postfix = self.generatePostfix.infixToPostfix(parsed_list)
        print(postfix)
        return postfix
        
