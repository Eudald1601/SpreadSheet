from .Operand import Operand
from .RangeCellsException import CircularDependencyException
class RangeCells(Operand):
    
    def __init__(self, cell1, cell2, cells) -> None:
        try:
            self.cell1 = cells[cell1]
        except:
            raise CircularDependencyException("THE CELL REFERENCE " + cell1 + " DOESN'T EXIST")
        try:
            self.cell2 = cells[cell2]
        except:
            raise CircularDependencyException("THE CELL REFERENCE " + cell2 + " DOESN'T EXIST")
        
        
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
            if column_a > column_b or row_a > row_b:
                raise CircularDependencyException("THE RANGE HAS NOT BEEN DEFINED PROPERLY")
            
            for cell in self.cells.values():
                try:
                    if cell.column >= column_a and cell.column <=column_b:
                        if cell.row >= row_a and cell.row <= row_b:
                            range_values.append(cell.content.getNumericalValue())
                except:
                    raise CircularDependencyException("THE RANGE HAS NOT BEEN DEFINED PROPERLY, THERE ARE EMPTY CELLS")
        return range_values
    
    def getCells(self):
        range_cells = []
        if self.cell1==self.cell2:
            range_cells = self.cell1
        else:
            
            column_a, row_a = self.cell1.getCoordinate()
            column_b, row_b = self.cell2.getCoordinate()
            for cell in self.cells.values():
                if cell.column >= column_a and cell.column <=column_b:
                    if cell.row >= row_a and cell.row <= row_b:
                        range_cells.append(cell)
           
        return range_cells
    