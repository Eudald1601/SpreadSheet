from PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.usecasesmarker.spreadsheet_controller_for_checker import ISpreadsheetControllerForChecker 
from PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.entities.bad_coordinate_exception import BadCoordinateException
from SpreadSheet.entities.SpreadSheet import SpreadSheet


class ConcreteSpreadsheetControllerForChecker(ISpreadsheetControllerForChecker):

    def __init__(self):
        self.spreadSheet = None
        


    def set_cell_content(self, coord, str_content):
        try:
            self.spreadSheet.insertContentInCell(cell_id=coord, content=str_content)        
        except:
            raise BadCoordinateException("the cellCoord argument does not represent a proper spreadsheet coordinate")
    
    