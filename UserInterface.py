# The UserInterface class provides methods for displaying the main menu and printing a spreadsheet.
from exceptions.SyntaxException import SyntaxException
class UserInterface:
   

    def __init__(self) -> None:
        pass
    
    def mainMenu(self):
        print (30 * "-", "MAIN MENU", 30 * "-")
        print("")
        print ("COMMANDS ALLOWED: YOU HAVE TO INTRODUCE THE COMMAND AND THE ARGUMENTS")
        print(60*"-")

        print ("E --EDIT CELL CELL")
        print("")
        print("NOW YOU HAVE TO INSERT WHICH CELL YOU WANT TO EDIT AND (A5) AND FOLLOWING WITH A SPACE THE CONTENT (FLOAT CONTENT, TEXT CONTENT OR FORMULA CONTENT)")
        print("---> TO INTRODUCE FLOAT CONTENT (EXAMPLE: 5.6)")
        print("---> TO INTRODUCE TEXT CONTENT (EXAMPLE: 5.5 or HELLOWORD)")
        print("---> TO INTRODUCE FORMULA CONTENT (EXAMPLE: =1+2 or =SUMA(A4;B7)) THE FIRST CHARACTER TO INTRODUCE MUST BE =" )
        print("")
        print("---> DIFFERENT TYPES OF FORMULA CONTENT:")
            
        print("-> =1.4+2.5 TO PERFORM BASIC OPERATIONS YOU MUST ENTER THE MULTIPLES OPERATORS AND THE OPERANDS ALLOWED (*, -, +, /)")
        print("-> =SUMA(A4;B5;D6) IT COMPUTES THE SUM OF THE VALUES OF THE CELLS IDENTIFIED IN IT'S ARGUMENT")
        print("-> =MIN(A3;B6;H5) IT COMPUTES THE MINIMUM OF THE VALUES OF THE CELLS IDENTIFIED IN IT'S ARGUMENT")
        print("-> =MAX(H6;F4;B6) IT RETURNS THE MAXIMUM VALUE OF THE VALUES OF THE CELLS IDENTIFIED IN ITS ARGUMENT")
        print("-> =PROMEDIO(Y7;U7;C3) IT RETURNS THE ARITHMETIC MEAN OF THE VALUES OF THE CELLS IDENTIFIED IN IT'S ARGUMENT")
        print("")
        print("-> YOU CAN COMBINE IN A SINGLE FORMULA CONTENT DIFFERENTS OPERATIONS")
        print(60*"-")
        print ("C --CREATE NEW SPREADSHEET")
        print(60*"-")
        print ("RF --READ COMMANDS FROM FILE")
        print(60*"-")
        print ("S --SAVE ACTUAL SPREADSHEET")
        print(60*"-")
        print ("L --LOAD A SPREADSHEET FROM FILE")
        print (67 * "-")
        return self.insertCommand()
 

    def insertCommand(self):
        """
        The function prompts the user for a command, passes it to a command syntax checker, and then applies
        the command.
        """
        choice = input("ENTER A COMMAND: ")
        parsed_choice = self.commandSyntax(choice)
        return parsed_choice
        
    
    

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
            self.idCellSyntaxControl(cell_id)
            content = parsed_command[2]
            return ("E", cell_id, content)

        if parsed_command[0] == "C":
            if len(parsed_command)==1 or len(parsed_command)>2:
                raise SyntaxException("MORE ARGUMENTS THAN EXPECTED (EXAMPLE: C Helloworld.txt)")
            
            if not parsed_command[1].endswith('.txt') or len(parsed_command[1].split("."))>2:      
                raise SyntaxException("THE NAME OF THE NEW SPREADSHEET IS NOT CORRECT (EXAMPLE: C Helloworld.txt)")  

            return ("C", parsed_command[1])
        
        if parsed_command[0] == "RF":
            pass

        if parsed_command[0] == "L":
            pass

        if parsed_command[0] == "S":
            pass

    
    def idCellSyntaxControl(self, cell_id):
        for id in cell_id:
            if id.isdigit()!=True and id.isalpha()!=True :
                print(id)
                raise SyntaxException("The ID of the CELL contains a non-alphanumerical value")
            
        i = 0
        while i < len(cell_id) and cell_id[i].isalpha():
            i+=1
        
        if i == 0 or i == len(cell_id) or not cell_id[i:].isdigit():
            raise SyntaxException("The order of the cell ID is not correct, remember (first letters and after numbers)")
        
        #Si el identificador de la celda es correcto no hace falta que devuelva nada
