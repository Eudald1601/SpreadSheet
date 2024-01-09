from SpreadSheet.frameworks.Loader import Loader
from SpreadSheet.frameworks.Saver import Saver

class FileController():
    def __init__(self, formulacomputing) -> None:
        self.loader = Loader(formulacomputing)
        self.saver = Saver()

    def saveFile(self, spreadsheet, path):
        self.saver.saveSpreadSheet(spreadsheet, path)
        
    def loadFile(self, path, spreadsheet):
        return self.loader.file_loader(path, spreadsheet)
    
    def loadCommands(self, path):
        return self.loader.loadCommands(path)