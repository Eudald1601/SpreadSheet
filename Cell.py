from Content import Content
from NumericalContent import NumericalContent
from TextualContent import TextualContent
from FormulaContent import FormulaContent

class Cell:
    def __init__(self, column, row, content_string) -> None:
        self.coordinate = (column, row)
        self.content : Content = self.insertNewContent(content_string)

    def getCoordinate(self):
        return self.coordinate
    
    def getContent(self):
        return self.content
    
    def insertNewContent(self, content_string):
    ## DUDA JUAN CARLOS: SI POR PARAMETRO LE PASO UN STRING CON EL CONTENIDO QUE QUIERO Y LE PASO A4 4.3 COMO DIFERENCIO QUE SEA UN CONTENIDO DE TIPO FLOAT O UNO DE TIPO STRING?
        
        #AISLAR ESTE IF HASTA TENER FORMULACOMPUTING
        if content_string[0] == "=":
            return FormulaContent(content_string)
        
    
        try:
            float(content_string)
            return NumericalContent(content_string)
            
        except:
            return TextualContent(content_string)
        
    