from Operand import Operand

class RangeCells(Operand):
    
    ##ATENCIO SI VOGUES QUE FOS IGUAL A2:B3 = B3:A2 hauria d'ordenar cell1 i cell2
    def __init__(self, cell1, cell2, cells) -> None:
        
        self.cell1 = cells[cell1]
        self.cell2 = cells[cell2]
        self.cells = cells
        if self.cell1 == self.cell2:
            super().__init__("CellReference")
        else:
            super().__init__("RangeCell")
        
    def getValue(self):
        range_values = []
        if self.cell1==self.cell2:
            range_values = self.cell1.content.getNumericalValue()
        else:
            
            column_a, row_a = self.cell1.getCoordinate()
            column_b, row_b = self.cell2.getCoordinate()
            for cell in self.cells.values():
                if cell.column >= column_a and cell.column <=column_b:
                    if cell.row >= row_a and cell.row <= row_b:
                        range_values.append(cell.content.getNumericalValue())
           
        return range_values