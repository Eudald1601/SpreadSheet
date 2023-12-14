from exceptions.SyntaxException import SyntaxException


### THIS CLASS CONTROLS THAT THE COMMAND INSERTED BY THE USER DOESN'T HAVE SYNTAX ERRORS, ELSE LUNCH EXCEPTION

class SyntaxSpreadSheetController:
    def __init__(self) -> None:
        pass

    def commandSyntax(self, command):
        
        try:
            parsed_command = command.split(" ")
        
        except Exception:
            raise SyntaxException("Can't not parse the command")
        
        if parsed_command[0]!="RF" and parsed_command[0]!="C" and parsed_command[0]!="E" and parsed_command[0]!="L" and parsed_command[0]!="S":
            raise SyntaxException("Command not correct")
        
        if parsed_command[0] == "E":
            
            if len(parsed_command)==1 or len(parsed_command)>3:
                raise SyntaxException("Parsing Error, you need to specify CELL ID and CONTENT (EXAMPLE: A4 4.5)")
            
            cell_id = parsed_command[1]
            
            for id in cell_id:
                if id.isdigit()!=True and id.isalpha()!=True :
                    print(id)
                    raise SyntaxException("The ID of the CELL contains a non-alphanumerical value")
                
            i = 0
            while i < len(cell_id) and cell_id[i].isalpha():
                i+=1
            
            if i == 0 or i == len(cell_id) or not cell_id[i:].isdigit():
                raise SyntaxException("The order of the cell ID is not correct, remember (first letters and after numbers)")
            

        if parsed_command[0] == "C":
            if len(parsed_command)==1 or len(parsed_command)>2:
                raise SyntaxException("MORE ARGUMENTS THAN EXPECTED (EXAMPLE: C Helloworld.txt)")
            
            if not parsed_command[1].endswith('.txt') or len(parsed_command[1].split("."))>2:      
                raise SyntaxException("THE NAME OF THE NEW SPREADSHEET IS NOT CORRECT (EXAMPLE: C Helloworld.txt)")  

        if parsed_command[0] == "RF":
            pass

        if parsed_command[0] == "L":
            pass

        if parsed_command[0] == "S":
            pass
