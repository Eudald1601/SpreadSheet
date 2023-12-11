from exceptions.SyntaxException import SyntaxException

class SyntaxCellController():
    
    def __init__(self) -> None:
        pass

    def is_Cell_Valid(self, content):
        list_contents = content.split(" ")
        if len(list_contents)==1 or len(list_contents)>2:
            raise SyntaxException("Parsing Error, you need to specify CELL ID and CONTENT (EXAMPLE: A4 4.5)")
        
        cell_id = list_contents[0]
        for id in cell_id:
            if id.isdigit()!=True and id.isalpha()!=True :
                print(id)
                raise SyntaxException("The ID of the CELL contains a non-alphanumerical value")
               
        i = 0
        while i < len(cell_id) and cell_id[i].isalpha():
            i+=1
        
        if i == 0 or i == len(cell_id) or not cell_id[i:].isdigit():
            raise SyntaxException("The order of the cell ID is not correct, remember (first letters and after numbers)")
        return cell_id