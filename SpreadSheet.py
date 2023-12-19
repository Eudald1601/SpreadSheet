# The SpreadSheet class represents a spreadsheet and allows for inserting content into cells and
# printing the spreadsheet.

from Cell import Cell
from PrinterSpreadSheet import PrinterSpreadSheet

class SpreadSheet:
    
    def __init__(self, name):
        self.name = name
        self.cells = {}
        self.printSpreadSheet = PrinterSpreadSheet()
    
    def getName(self):
        return self.name
   

    def insertContentInCell(self, cell_id, content):
        """
        The function inserts content into a cell if the cell does not already exist.
        
        :param edit_cell: The `edit_cell` parameter is a tuple that contains three elements: `column`,
        `row`, and `content`. The `column` and `row` represent the coordinates of the cell where the content
        will be inserted, and `content` is the actual content that will be inserted into the cell
        """
        #SE TIENE QUE TENER EN CUENTA QUE AAAA4 ES UN VALOR VALIDO 

        if len(self.cells)==0 or not cell_id in self.cells:
            cell = Cell(cell_id, content)
            self.cells[cell_id] = cell

        else:
            existing_cell = self.cells[cell_id]
            existing_cell.insertNewContent(content)


    def printMyself(self):
        self.printSpreadSheet.printSpreadSheet(self.cells, self.name)

       