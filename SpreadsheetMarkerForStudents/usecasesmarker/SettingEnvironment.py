from usecasesmarker.spreadsheet_controller_for_checker import ISpreadsheetControllerForChecker
import sys
import os
sys.path.append(os.path.join("../../",os.getcwd()))
print(sys.path)
from SpreadSheet.usecases.SpreadSheetController import SpreadSheetController

class SettingEnvironment(ISpreadsheetControllerForChecker):
    def __init__(self) -> None:
        self.controller = SpreadSheetController()
        self.controller.applyCommand(["C", "marker_save_test.s2v"])
        super().__init__()
        
    def set_cell_content(self, coord, str_content):
        content = ["E", coord, str(str_content)]
        self.controller.applyCommand(content)
        
    def get_cell_content_as_float(self, coord):
        cell = self.controller.spreadSheet.cells[coord]
        return cell.content.getNumericalValue()
    
    def get_cell_content_as_string(self, coord):
        cell = self.controller.spreadSheet.cells[coord]
        return cell.content.getTextualValue()
    
        
    def get_cell_formula_expression(self, coord):
        cell = self.controller.spreadSheet.cells[coord]
        if cell.content.typeOfContent()=="FormulaContent":
            formulastring = cell.content.getValue()
            finalformulastring = formulastring
        return finalformulastring
    
    def save_spreadsheet_to_file(self, s_name_in_user_dir):
        path = os.path.join(os.getcwd(),s_name_in_user_dir)
        self.controller.applyCommand(["S", path])

    def load_spreadsheet_from_file(self, s_name_in_user_dir):
        path = os.path.join(os.getcwd(),"SpreadsheetMarkerForStudents/markerrun/")
        path = path + "/" + s_name_in_user_dir
        self.controller.applyCommand(["L", path])
        pass