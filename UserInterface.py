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
 
        
