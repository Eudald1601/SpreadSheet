from Content import Content
from ContentManager import ContentManager

class FormulaContent(Content):
    def __init__(self, content, formulaComputing) -> None:
        super().__init__("FormulaContent")
        self.contentManager = ContentManager(content, formulaComputing)
        self.content = content

    def calculateFormula(self, cells):
        self.content = self.contentManager.calculateFormulaValue(cells)
    
    def getNumericalValue(self):
        
        return self.content
    
    
    def getTextualValue(self):
        return str(self.content)
    

        
    