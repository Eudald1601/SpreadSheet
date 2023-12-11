from Cell import Cell
from SyntaxCellController import SyntaxCellController

class SpreadSheet:
    
    def __init__(self) -> None:
        self.name = ""
        self.path = ""
        self.cells = []
        self.syntaxCellController = SyntaxCellController()
        



    def setName(self, name):
        self.name = name

    def setPath(self, path):
        self.path = path

    def searchCell(self, content):
        cell_id = self.syntaxCellController.is_Cell_Valid(content)
        