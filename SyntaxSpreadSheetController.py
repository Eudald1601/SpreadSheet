from exceptions.SyntaxException import SyntaxException

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