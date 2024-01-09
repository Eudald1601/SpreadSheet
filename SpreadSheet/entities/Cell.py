# The Cell class represents a cell in a spreadsheet and can contain different types of content such as
# numerical, textual, or formulaic.

from Content.entities.Content import Content
from Content.entities.NumericalContent import NumericalContent
from Content.entities.TextualContent import TextualContent
from Content.entities.FormulaContent import FormulaContent
from SpreadsheetMarkerForStudents.entities.circular_dependency_exception import CircularDependencyException
class Cell:
    ##ME INTERESA GUARDAR POR SEPARADO LAS FILAS Y COLUMNAS PARA PODER PRINTEARLAS MEJOR
    def __init__(self, cell_id, formulaComputing, spreadsheet) -> None:
        column = ""
        row = ""
        
        for v in cell_id:
            if v.isalpha():
                column = column + v
            elif v.isdigit():
                row= row + v
        self.row = int(row)
        self.column = column
        self.spreadsheet = spreadsheet
        ##DUDA JUAN CARLOS: DUDO MUCHO QUE TE GUSTE ESTO
        self.content : Content
        self.formulaComputing = formulaComputing
        self.iDependOn = []
        self.dependOnMe = {}
    def getCoordinate(self):
        return self.column, self.row
    
    def getContent(self):
        return self.content
    
    def insertNewContent(self, content_string):
        """
        The function `insertNewContent` takes a string as input and returns an instance of a specific
        content type (FormulaContent, NumericalContent, or TextualContent) based on the content of the
        string.
        
        :param content_string: The `content_string` parameter is a string that represents the content you
        want to insert. It can be either a numerical value (integer or float) or a textual value (string)
        :return: an instance of either the FormulaContent, NumericalContent, or TextualContent class,
        depending on the type of content_string passed as a parameter.
        """
    ## DUDA JUAN CARLOS: SI POR PARAMETRO LE PASO UN STRING CON EL CONTENIDO QUE QUIERO Y LE PASO A4 4.3 COMO DIFERENCIO QUE SEA UN CONTENIDO DE TIPO FLOAT O UNO DE TIPO STRING?
        
        #AISLAR ESTE IF HASTA TENER FORMULACOMPUTING
        string = content_string.strip()
        if string[0] == "=":
            formulacontent = FormulaContent(content_string, self.formulaComputing, self.spreadsheet.cells)
            self.proveNoCircularExeption(content_string)
            formulacontent.calculateFormula() #LE PASARIA SOLO LAS DEPENDING CELLS PERO TENGO PROBLEMAS CON LAS OPERACIONES CON RANGOS NO SON SOLO UNA CELDA
            newdepend = formulacontent.getCircularDependences()
            if len(self.dependOnMe) != 0:
                eliminar = set(self.dependOnMe) - set(newdepend)
            else:
                eliminar = set()
            
            self.iDependOn = newdepend
            self.setDpendOnMe(list(eliminar))

            self.content = formulacontent
        else:
            try:
                float(content_string)
                self.content = NumericalContent(content_string)
                
            except:
                self.content = TextualContent(content_string)
        
            
        
                           
        if len(self.dependOnMe)!=0:
            for cell in self.dependOnMe.values():
                cell.recalculateFormula()
                
                

    def recalculateFormula(self):
        try:
            self.content.calculateFormula()     
        except:
            raise CircularDependencyException()
        
    def setDpendOnMe(self, eliminar):
        if len(self.iDependOn) != 0:
            celda = self.column + str(self.row)
            for cell in self.iDependOn:
                if eliminar != None:
                    for e in eliminar:
                        i = 0
                        for delete in cell.iDependOn:
                            todele = delete.column + str(delete.row)
                            if todele == celda:
                                del cell.iDependOn[i]
                            i=+1
                celda = self.column+str(self.row)
                cell.dependOnMe[celda] = self
                
    def proveNoCircularExeption(self, string):
        if len(self.dependOnMe) != 0:
            postfix = self.formulaComputing.computeFormula(string)
            
            for iscell in postfix:
                a = self.formulaComputing.parse.is_valid_cell(iscell)
                if a:
                    idependon = iscell
                    for dependonme in self.dependOnMe.values():
                        dependonme.proveNoCircularExeption(string)
                        dependonmecellid = dependonme.column + str(dependonme.row)
                        if idependon== dependonmecellid:
                            raise CircularDependencyException("")       
                
