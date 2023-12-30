from Operand import Operand

class Number(Operand):
    def __init__(self, number) -> None:
        super().__init__("Number")
        self.number = number
        
    def getValue(self):
        return float(self.number)