from Cell import Cell

class SpreadSheet:
    
    def __init__(self, name):
        self.name = name
        self.cells = []

    
    def getName(self):
        return self.name
   

    def insertContentInCell(self, edit_cell):
        column, row, content = edit_cell[0], edit_cell[1], edit_cell[2:]
        if len(self.cells)==0 or self.cellExists(column,row) == None:
            cell = Cell(column, row)
            cell.insertNewContent(content)
            self.cells.append(cell)

        else:
            pass


    def cellExists(self, column, row):
        for cell in self.cells:
            if cell.getCoordinate() == (column, row):
                return cell
        
        return None




       