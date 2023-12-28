

# Python program to convert infix expression to postfix
import re
 
# Class to convert the expression
class GeneratePostfix:
    #A4-B2/SUMA(A2:A4;B4)   --> 

    # A4      POSTFIX  A4                         STACK 
    # -       POSTFIX  A4                         STACK -
    # B2      POSTFIX  A4 B2                      STACK -
    # /       POSTFIX  A4 B2                      STACK - /
    # SUMA    POSTFIX  A4 B2                      STACK - / SUMA
    # (       POSTFIX  A4 B2                      STACK - / SUMA (
    # A2      POSTFIX  A4 B2 A2                   STACK - / SUMA (
    # :       POSTFIX  A4 B2 A2                   STACK - / SUMA ( :
    # A4      POSTFIX  A4 B2 A2 A4 :              STACK - / SUMA ( 
    # ;       POSTFIX  A4 B2 A2 A4 :              STACK - / SUMA ( ;
    # B4      POSTFIX  A4 B2 A2 A4 : B4 ;         STACK - / SUMA ( 
    # )       POSTFIX  A4 B2 A2 A4 : B4 ; SUMA / -
 
    # Constructor to initialize the class variables
    def __init__(self):
        self.precedence = {'+': 2, '-': 2, '*': 3, '/': 3, "PROMEDIO":10, "SUMA":10, "MAX":10, "MIN":10, ":":10, ";":10}
        self.functions = ["PROMEDIO", "SUMA", "MAX", "MIN"]
        
    def infixToPostfix(self, tokens):
        stack = []
        postfix = []
        i = 0
        for i in range(len(tokens)):
            if self.precedence.get(tokens[i], False):
                if len(stack) == 0:
                    stack.append(tokens[i])
                    
                elif self.precedence.get(stack[len(stack)-1], False) < self.precedence.get(tokens[i], False):
                    stack.append(tokens[i])
                
                else:
                    while len(stack) > 0 and self.precedence.get(stack[len(stack)-1], False) >= self.precedence.get(tokens[i], False):
                        last = stack[len(stack)-1]
                        postfix.append(last)
                        stack.pop()
        
                    stack.append(tokens[i])
            
                
         
            elif tokens[i] == "(":
                stack.append(tokens[i])
                
            
            elif tokens[i] == ")":
                while len(stack) > 0 and self.precedence.get(stack[len(stack)-1], False) >= self.precedence.get(tokens[i], False):
                    last = stack[len(stack)-1]
                    if last != "(":
                        postfix.append(last)
                    stack.pop()
            
            else:
                postfix.append(tokens[i])
                
            print(postfix, stack)
        return postfix, stack
        
        # operand = False
        # range = False
        # i = 0
        # for token in tokens:
            
        #     if operand and token != "(" and token not in self.functions:
        #         operand = False
        #         stack.pop(i)
        #         postfix.append(token)
        #         postfix.append(";")
                
                
        #     elif token == ")":
                
        #     elif token == ":":
        #         stack.append(token)
        #         range = True   
                   
        #     elif self.is_valid_cell(token) and range:
        #         range = False
        #         stack.pop(i)
        #         postfix.append(token)
        #         postfix.append(":")       
                 
        #     elif self.is_valid_cell(token) or token.isdigit():
        #         postfix.append(token)
                
        #     elif self.precedence.get(token, False):
        #         stack.append(token)
            
        #     elif token == ";":
        #         stack.append(token)
        #         operand = True
    
        #     i+=1 
    def is_valid_cell(self, cell):
        # Verifica si la celda es válida
        if isinstance(cell, str) and re.match(r'^[A-Z]+[1-9]\d*$', cell):    # Modificar si las celdas pueden ser más largas
            return True
        return False        