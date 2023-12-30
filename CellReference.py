from Operand import Operand

class CellReference(Operand):
    
    def __init__(self, cell) -> None:
        self.cell = cell
        super().__init__("CellReference")
        
    def getValue(self):
        return self.cell.content.getNumericalValue()
        
