import re

class Parser:
   
    def __init__(self) -> None:
        self.function = ["SUMA", "PROMEDIO", "MAX", "MIN"]
        self.operator = ["+", "-", "*", "/"]
        self.others = [";", ":", "(", ")"]
    
    def parse(self, tokens):
        opening_paren_count = 0
        last_token = None
        closing_paren_count = 0
        for token in tokens:
            
            ### EL PRIMER TOKEN NO PUDE SER NI UN OPERADOR NI UN CARACTER ESPECIAL
            print(last_token , token)
            if last_token == None and (token in self.operator or token in self.others):
                print("Error el primer token")
            
            if token == "(":
                opening_paren_count+=1
            
            if token == ")":
                closing_paren_count+=1
            
            ### DOS CARACTERES NO PUEDEN SER EL MISMO A NO SER QUE SEAN PARENTESIS CERRADOS I CIERREN LOS DE FUNCIONES 
            if not self.no_type_repited(last_token, token):
                if closing_paren_count != opening_paren_count:
                    continue
                print("Multiples tokens repetidos")
            
            ## SE DEBE ASEGURAR QUE AL INICIO DE UNA FUNCION SUMA( EL SIGUIENTE TOKEN SEA UN PARENTESIS
            if  last_token in self.function and not token == "(":
                print("La funcion no empieza con (")
                raise Exception
            
            ## DESPUES DE UN PARENTESIS SOLO PUEDE VENIR UNA CELDA O UN NUMERO O OTRA FUNCION
            if last_token == "(" and (token in self.operator or token in self.others):
                print("Error despues del parentesis de la funcion")
                raise Exception
            
            ## DESPUES DE : DEBE VENIR OTRA CELDA
            if last_token == ":" and not self.is_valid_cell(token):
                print("Rango mal puesto")
            
            ## SE TERMINA UNA FUNCION DEBE SEGUIR CON UN OPERANDO CON UN ; SI ESTA DENTRO DE OTRA
            if last_token == ")":
                print(opening_paren_count, closing_paren_count)
                if opening_paren_count != closing_paren_count:
                    if token != ";":
                        raise Exception
                
                
            last_token = token
        return tokens
    
    def is_valid_cell(self, cell):
        # Verifica si la celda es válida
        if isinstance(cell, str) and re.match(r'^[A-Z]+[1-9]\d*$', cell):    # Modificar si las celdas pueden ser más largas
            return True
        return False
    
    def no_type_repited(self, last_token, token):
        if self.is_valid_cell(last_token) and self.is_valid_cell(token):
            print("Celda y celda")
            return False
        
        elif last_token in self.function and token in self.function:
            print("funcion y funcion")
            return False
        
        elif last_token in self.operator and token in self.operator:
            print("operador y operador")
            return False
        
        elif last_token == ")" and token == ")":
            print("parentesis ))")
            return True

        elif last_token in self.others and token in self.others:
            if last_token == ")":
                return True
            print(";; o :;")
            return False
        
        return True
        
        