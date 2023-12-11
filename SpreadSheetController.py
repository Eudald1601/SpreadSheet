from UserInterface import UserInterface
from SpreadSheet import SpreadSheet
from SyntaxSpreadSheetController import SyntaxSpreadSheetController
class SpreadSheetController:
    
    def __init__(self):
    
        self.UI = UserInterface()
        self.spreadSheet = SpreadSheet()
        self.syntaxspreadsheetcontroller = SyntaxSpreadSheetController()
    
    def showMenu(self):
        self.UI.mainMenu()
        
    def insertCommand(self):
        choice = input("ENTER A COMMAND: ")
        self.syntaxspreadsheetcontroller.commandSyntax(choice)
        self.applyCommand(choice)
        
    
    def applyCommand(self, command):
        if command[0] == 'E':
            self.spreadSheet.searchCell(command[2:])

    