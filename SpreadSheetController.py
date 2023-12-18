from UserInterface import UserInterface
from SpreadSheet import SpreadSheet
from SyntaxSpreadSheetController import SyntaxSpreadSheetController
from exceptions.SpreadSheetCommandException import SpreadSheetCommandException
class SpreadSheetController:
    
    def __init__(self):
    
        self.UI = UserInterface()
        self.spreadSheet = None
        self.syntaxspreadsheetcontroller = SyntaxSpreadSheetController()
    
    def showMenu(self):
        self.UI.mainMenu()
        
    def insertCommand(self):
        choice = input("ENTER A COMMAND: ")
        self.syntaxspreadsheetcontroller.commandSyntax(choice)
        self.applyCommand(choice)
        
    
    ##### DUDA JUAN CARLOS: NOSOTROS PRIMEROS COMRPROBAMOS QUE LA SINTAXI QUE SE PRETENDE INTRODUCIR SEA CORRECTA, DESPUÉS CONTROLAMOS LA LÓGICA DEL CONTROLADOR (EJEMPLO: NO PUEDES EDITAR EL FICHERO SI PREVIAMENTE NO LO HAS CREADO NI CARGADO)

    def applyCommand(self, command):
        co = command.split(" ")
        if co[0] == 'E':
            if self.spreadSheet == None:
                raise SpreadSheetCommandException("YOU ARE TRYING TO EDIT A CELL BEFORE CREATING A SPREADSHEET")
            self.spreadSheet.insertContentInCell(command[2:])  ##LE PASO DIRECTO STRING CELL CONTENT (A4 4.4) NÓTESE QUE EN ESTE PUNTO LA ASEGURO QUE LA SINTAXI ES CORRECTA
            self.spreadSheet.printMyself()
        elif co[0] == 'C':
            if self.spreadSheet != None and self.spreadSheet.getName()==co[1]:
                raise SpreadSheetCommandException("THE NAME OF THE NEW SPREADSHEET IS ALREADY USED")
            self.spreadSheet = SpreadSheet(co[1])
        
        
        elif co[0] == 'SF':
            pass

        elif co[0] == 'L':
            pass

        elif co[0] == 'S':
            pass

    