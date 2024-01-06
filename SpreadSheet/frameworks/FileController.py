from SpreadSheet.frameworks.Loader import Loader
from SpreadSheet.frameworks.Saver import Saver

class FileController():
    def __init__(self) -> None:
        self.loader = Loader()
        self.saver = Saver()

    def saveFile(self, spreadsheet, path):
        self.saver.saveSpreadSheet(spreadsheet, path)
        
    def loadFile(self, path, spreadsheet):
        return self.loader.file_loader(path, spreadsheet)