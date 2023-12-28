# The Cell class represents a cell in a spreadsheet and can contain different types of content such as
# numerical, textual, or formulaic.

from Content import Content
from NumericalContent import NumericalContent
from TextualContent import TextualContent
from FormulaContent import FormulaContent

class Cell:
    ##ME INTERESA GUARDAR POR SEPARADO LAS FILAS Y COLUMNAS PARA PODER PRINTEARLAS MEJOR
    def __init__(self, cell_id) -> None:
        column = ""
        row = ""
        for v in cell_id:
            if v.isalpha():
                column = column + v
            elif v.isdigit():
                row= row + v
        self.row = int(row)
        self.column = column
        ##DUDA JUAN CARLOS: DUDO MUCHO QUE TE GUSTE ESTO
        self.content : Content
        
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
        if content_string[0] == "=":
            self.content = FormulaContent(content_string)


        try:
            float(content_string)
            self.content = NumericalContent(content_string)
            
        except:
            self.content = TextualContent(content_string)
        
    