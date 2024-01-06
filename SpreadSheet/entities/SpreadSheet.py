# The SpreadSheet class represents a spreadsheet and allows for inserting content into cells and
# printing the spreadsheet.

from SpreadSheet.entities.Cell import Cell
from SpreadSheet.frameworks.PrinterSpreadSheet import PrinterSpreadSheet
from SpreadSheet.frameworks.Saver import Saver
from SpreadSheet.frameworks.Loader import Loader


class SpreadSheet:
    
    def __init__(self, name, formulaComputing):
        self.name = name
        self.cells = {}
        self.printSpreadSheet = PrinterSpreadSheet()
        self.formulaComputing = formulaComputing
        self.saver = Saver()
        self.loader=Loader()
    
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
            cell = Cell(cell_id, self.formulaComputing, self)
        else:
            cell = self.cells[cell_id]
        
    
        cell.insertNewContent(content)
        self.cells[cell_id] = cell
        
    def printMyself(self):
        self.printSpreadSheet.printSpreadSheet(self.cells, self.name)

    def file_saver(self,name):
        self.saver.saveSpreadSheet(name,self.cells)

    def file_loader(self,namefile):
        loaded_dic=self.loader.loadSpreadSheet(namefile)
        loaded_cells = {}

        for clave, valor in loaded_dic.items():
            # Crea una instancia de Cell con el contenido
            cell_instance = Cell(clave, self.formulaComputing, self)
            cell_instance.insert(valor)
            # Agrega la instancia de Cell al nuevo diccionario
            loaded_cells[clave] = cell_instance
            
        self.printSpreadSheet.printSpreadSheet(loaded_cells,namefile)


    