# The SpreadSheetController class is responsible for handling user commands, validating their syntax,
# and applying the corresponding actions on a spreadsheet.


from UI.UserInterface import UserInterface
from SpreadSheet.entities.SpreadSheet import SpreadSheet
from SpreadSheet.usecases.SpreedSheetCommandException import SpreadSheetCommandException
from SpreadSheet.adapters.FormulaComputing import FormulaComputing
from SpreadSheet.frameworks.Loader import Loader
class SpreadSheetController:
    
    def __init__(self):
    
        self.UI = UserInterface()
        self.spreadSheet = None
        self.formulaComputing = FormulaComputing()
        self.loader = Loader()

    def showMenu(self):
        command = self.UI.mainMenu()
        self.applyCommand(command)
    ##### DUDA JUAN CARLOS: NOSOTROS PRIMEROS COMRPROBAMOS QUE LA SINTAXI QUE SE PRETENDE INTRODUCIR SEA CORRECTA, DESPUÉS CONTROLAMOS LA LÓGICA DEL CONTROLADOR (EJEMPLO: NO PUEDES EDITAR EL FICHERO SI PREVIAMENTE NO LO HAS CREADO NI CARGADO)

    def applyCommand(self, command):
        """
        The function `applyCommand` takes a command as input and performs different actions based on the
        command type.
        
        :param command: The `command` parameter is a string that represents a command to be executed. It is
        split into a list of words using the space character as the delimiter. The first word in the list
        (`co[0]`) represents the type of command to be executed. The remaining words in the list are the 
        contents to process`
        """
        print(command)
        
        if command[0] == 'E': #Edit
            if self.spreadSheet == None:
                raise SpreadSheetCommandException("YOU ARE TRYING TO EDIT A CELL BEFORE CREATING A SPREADSHEET")
            try:
                self.spreadSheet.insertContentInCell(cell_id=command[1], content=command[2])  ##LE PASO DIRECTO STRING CELL & CONTENT (A4 4.4) NÓTESE QUE EN ESTE PUNTO LA ASEGURO QUE LA SINTAXI ES CORRECTA
            except:
                raise SpreadSheetCommandException("THE CONTENT CAN NOT BE INTRODUCED IN CELL BECAUSE THE CELL DEPENDS ON ANOTHER")
            self.spreadSheet.printMyself()
            
        elif command[0] == 'C': #Create
            if self.spreadSheet != None and self.spreadSheet.getName()==command[1]:
                raise SpreadSheetCommandException("THE NAME OF THE NEW SPREADSHEET IS ALREADY USED")
            self.spreadSheet = SpreadSheet(command[1], self.formulaComputing)
            print("SpreadSheet created")
        
        
        elif command[0] == 'RF':
            try:
                c=self.loader.loadCommands(command[1])
                for d in c:
                    self.applyCommand(d)
            except:
                raise SpreadSheetCommandException("THE FILE CAN NOT BE READ")
            

        elif command[0] == 'L':
            try:
                self.spreadSheet = SpreadSheet(command[1], self.formulaComputing)
                self.spreadSheet.file_loader(command[1])
            except:
                raise SpreadSheetCommandException("THE SPREADSHEET CAN NOT BE LOAD")
            
        elif command[0] == 'S':
            if self.spreadSheet == None:
                raise SpreadSheetCommandException("YOU ARE TRYING TO SAVE A SPREADSHEET BEFORE CREATING A SPREADSHEET")
            try:
                self.spreadSheet.file_saver(command[1])
            except:
               raise SpreadSheetCommandException("THE SPREADSHEET CAN NOT BE SAVED")

    